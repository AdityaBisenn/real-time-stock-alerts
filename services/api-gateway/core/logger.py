from loguru import logger
import os

log_file = os.getenv("LOG_FILE", "logs/api_gateway.log")
logger.add(log_file, rotation="10MB", level="INFO")

def log_request(message):
    logger.info(message)
