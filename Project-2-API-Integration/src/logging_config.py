import logging

# Configure logging
def setup_logging():
    logging.basicConfig(
        filename='../logs/app.log',  # Log to a file in the logs directory
        level=logging.INFO,          # Capture logs from INFO level and above
        format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
    )

# Call the setup function
setup_logging()