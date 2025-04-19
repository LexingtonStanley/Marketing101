from app.helper_funcs.database.database_connector import DatabaseConnector
import yaml
import os
from psycopg2 import sql
import logging as x  # I'm assuming x is your logger


class Freefallcentral_Database:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.table_name = None
        self.schema_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                       'schemas', 'tables')

    def _load_schema(self, table_name):
        """
        Load table schema from a YAML file.

        Args:
            table_name (str): Name of the table to load the schema for

        Returns:
            dict: The loaded schema or None if file not found
        """
        schema_path = os.path.join(self.schema_dir, f"{table_name}.yaml")

        try:
            with open(schema_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            x.error(f"Schema file not found for table '{table_name}' at {schema_path}")
            return None
        except Exception as e:
            x.exception(f"Error loading schema for '{table_name}': {e}")
            return None

    @staticmethod
    def _generate_create_table_sql(schema):
        """
        Generate CREATE TABLE SQL statement from schema definition.

        Args:
            schema (dict): The schema definition loaded from YAML

        Returns:
            sql.SQL: SQL query to create the table
        """
        if not schema:
            return None

        # Build the columns part of the SQL
        columns_sql = []
        for column in schema['columns']:
            column_def = f"{column['name']} {column['type']}"
            if column.get('constraints'):  # Use get() to avoid KeyError if constraints is None
                column_def += f" {column['constraints']}"
            columns_sql.append(column_def)

        # Join all column definitions with commas
        columns_sql_str = ",\n                            ".join(columns_sql)

        # Build the complete CREATE TABLE statement as a string first
        create_sql_str = f"""
            CREATE TABLE {{table}} (
                            {columns_sql_str}
            )
            """

        # Convert to SQL object
        create_sql = sql.SQL(create_sql_str)

        return create_sql

    async def check_and_create_table(self, table_name):
        """
        Asynchronously checks if the table exists and creates it if it doesn't
        using the schema defined in YAML.

        Args:
            table_name (str): Name of the table to check/create
        """
        self.table_name = table_name

        try:
            # Load schema from YAML
            schema = self._load_schema(table_name)
            if not schema:
                x.error(f"Cannot create table '{table_name}' - schema not found")
                return False

            # Ensure database connector is initialized
            if not getattr(self.db_connector, 'initialized', False):
                await self.db_connector.init()

            async with self.db_connector.get_cursor() as cur:
                # Check if table exists
                await cur.execute(
                    """
                    SELECT EXISTS (SELECT 1
                                   FROM information_schema.tables
                                   WHERE table_name = %s)
                    """,
                    (self.table_name,)
                )
                exists_result = await cur.fetchone()

                # Handle the result as a dictionary (RealDictCursor) not as a list
                table_exists = exists_result.get('exists', False) if exists_result else False

                if not table_exists:
                    x.info(f"Table '{self.table_name}' does not exist. Creating...")

                    # Generate CREATE TABLE SQL from schema
                    create_sql = self._generate_create_table_sql(schema)
                    if not create_sql:
                        return False

                    # Format with table name and execute
                    formatted_sql = create_sql.format(table=sql.Identifier(self.table_name))
                    await cur.execute(formatted_sql)
                    x.info(f"Table '{self.table_name}' created successfully.")
                else:
                    x.info(f"Table '{self.table_name}' already exists.")

                return True

        except Exception as e:
            x.exception(f"Error checking or creating table '{self.table_name}': {e}")
            raise