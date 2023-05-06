import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE_NAME = "app.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

LOG_FORMAT = "[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s"
formatter = logging.Formatter(LOG_FORMAT)

handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=1024*1024, backupCount=5)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info("Logger configured successfully")

