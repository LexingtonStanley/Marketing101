import os
import aiopg
import psycopg2.extras
from logger import setup_logger
from contextlib import asynccontextmanager
from dotenv import load_dotenv, find_dotenv
# Configure the logger
x = setup_logger()
load_dotenv(find_dotenv('env.env'))
class DatabaseConnector:
    """
    A singleton class that manages an asynchronous pool of PostgreSQL database connections via aiopg.
    It provides async context manager capabilities for safely acquiring and releasing
    database cursors and connections without blocking the main thread.
    """
    _instance = None
    _already_initialised = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self.__class__._already_initialised:
            return
        self.initialized = False
        self.pool = None
        self.port = None
        self.host = None
        self.password = None
        self.user = None
        self.dbname = None
        self.__class__._already_initialised = True

    async def init(self):
        if getattr(self, 'initialized', False):
            return

        try:
            x.debug("Initializing MarketDatabaseConnector asynchronously")

            self.dbname = os.getenv('MARKET_DATABASE_NAME', 'freefallcentral')
            self.user = os.getenv('POSTGRES_USER', 'postgres')
            self.password = os.getenv('POSTGRES_PASSWORD')
            self.host = os.getenv('POSTGRES_HOST', '172.27.144.1')
            self.port = int(os.getenv('POSTGRES_PORT', 5432))

            if not self.password:
                raise ValueError("Environment variable 'POSTGRES_PASSWORD' is not set.")

            dsn = (
                f"dbname={self.dbname} user={self.user} password={self.password} "
                f"host={self.host} port={self.port}"
            )

            x.info("Async connector configured")
            self.pool = await aiopg.create_pool(dsn=dsn, minsize=1, maxsize=50)
            x.info("Asynchronous connection pool created successfully")
            self.initialized = True
        except Exception as e:
            x.exception("MarketDatabaseConnector Initialization Error: %s", e)
            raise

    async def close_pool(self):
        if getattr(self, "pool", None) is not None:
            self.pool.close()
            await self.pool.wait_closed()
            x.debug("Connection pool closed gracefully.")
            self.pool = None
            self.initialized = False

    @asynccontextmanager
    async def get_cursor(self):
        """
        Acquire a cursor using a RealDictCursor so that rows are returned as dictionaries.
        """
        # Make sure we're initialized before trying to use the pool
        if not getattr(self, 'initialized', False) or self.pool is None:
            await self.init()
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                    yield cur
        except Exception as e:
            x.exception("Error in 'get_cursor': %s", e)
            raise

    async def get_connection(self):
        # Make sure we're initialized before trying to use the pool
        if not getattr(self, 'initialized', False) or self.pool is None:
            await self.init()
        try:
            conn = await self.pool.acquire()
            x.debug("Successfully retrieved a connection from the async pool.")
            return conn
        except Exception as e:
            x.exception("Error while getting a connection from the async pool: %s", e)
            raise

    async def put_connection(self, conn):
        try:
            await self.pool.release(conn)
            x.debug("Successfully returned a connection to the async pool.")
        except Exception as e:
            x.exception("Error while returning a connection to the async pool: %s", e)
            raise
