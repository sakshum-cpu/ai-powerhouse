"""Main entry point for AI Powerhouse"""
from config import settings
from utils.logger import get_logger
from chatbot.chatbot import Chatbot
from agent.agent import Agent
from code_generator.generator import CodeGenerator

logger = get_logger(__name__)


def main():
    """Main function"""
    logger.info(f"Starting {settings.app_name}")
    logger.info(f"Using model: {settings.llm_model}")
    
    # This is a placeholder main function
    # See examples/ directory for actual usage
    
    if settings.debug:
        logger.info("Debug mode enabled")


if __name__ == "__main__":
    main()
