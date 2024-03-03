import sys
from app.core.config import settings
from loguru import logger

logger.remove()
logger.add(sys.stdout, colorize=True, format=settings.LOG_FORMAT, level=settings.LOG_LEVEL)