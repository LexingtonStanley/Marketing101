import logging

def setup_logger():
    """
    Sets up the application's logger.
    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger("liquidations_logger")  # Use a consistent name for your app's logger
    logger.setLevel(logging.INFO)  # Set the desired logging level

    # Check if the logger already has handlers to avoid duplication
    if not logger.handlers:
        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Set the console handler's level

        # Create a formatter
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add the console handler to the logger
        logger.addHandler(console_handler)

        # Example: Add a file handler (optional)
        file_handler = logging.FileHandler('liquidations.log')
        file_handler.setLevel(logging.INFO)  # Set the file handler's level
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger