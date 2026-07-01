"""Example: Using the Chatbot"""
import asyncio
from chatbot.chatbot import Chatbot
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Run chatbot example"""
    logger.info("=" * 50)
    logger.info("AI Powerhouse - Chatbot Example")
    logger.info("=" * 50)
    
    # Initialize chatbot
    chatbot = Chatbot(
        name="Assistant",
        system_prompt="You are a helpful AI assistant. Be concise and accurate."
    )
    
    # Example conversations
    questions = [
        "What is machine learning?",
        "How does deep learning differ from machine learning?",
        "Can you give me 3 tips for learning AI?",
    ]
    
    for question in questions:
        logger.info(f"\nUser: {question}")
        try:
            response = chatbot.chat(question)
            logger.info(f"Assistant: {response}")
        except Exception as e:
            logger.error(f"Error: {str(e)}")
    
    # Print conversation stats
    logger.info(f"\nConversation Stats:")
    stats = chatbot.get_stats()
    for key, value in stats.items():
        logger.info(f"  {key}: {value}")
    
    # Print conversation history
    logger.info(f"\nConversation History:")
    history = chatbot.get_history()
    for i, msg in enumerate(history, 1):
        logger.info(f"  {i}. [{msg['role'].upper()}] {msg['content'][:50]}...")


if __name__ == "__main__":
    main()
