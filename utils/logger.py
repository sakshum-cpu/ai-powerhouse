"""Logger configuration for AI Powerhouse"""
import logging
from config import settings

def get_logger(name):
    """Get configured logger instance"""
    logger = logging.getLogger(name)
    logger.setLevel(settings.log_level)
    
    # Create console handler
    handler = logging.StreamHandler()
    handler.setLevel(settings.log_level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger
