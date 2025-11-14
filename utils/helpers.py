import logging
import time

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger("AwareAI")

def log(msg, level="info"):
    """Convenience logger."""
    if level == "info":
        logger.info(msg)
    elif level == "warn":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)
    else:
        logger.debug(msg)

def timestamp():
    """Return current timestamp as string."""
    return time.strftime("%Y-%m-%d %H:%M:%S")
