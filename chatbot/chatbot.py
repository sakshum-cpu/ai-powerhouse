"""Chatbot implementation"""
from typing import Optional, Dict, Any
from chatbot.memory import Memory
from utils.llm import get_llm
from utils.logger import get_logger
from utils.errors import AIError

logger = get_logger(__name__)

class Chatbot:
    """Intelligent chatbot with memory management"""
    
    def __init__(self, name="NEURON", system_prompt=None):
        """Initialize chatbot"""
        self.name = name
        self.memory = Memory()
        self.system_prompt = system_prompt or f"""
You are {name}, an intelligent AI assistant. 
You are helpful, harmless, and honest.
Provide clear, concise, and accurate responses.
Remember context from previous conversations.
        """
        self.llm = get_llm()
        logger.info(f"Chatbot '{name}' initialized")
    
    def chat(self, user_input: str) -> str:
        """Chat with the bot"""
        try:
            # Add user message to memory
            self.memory.add_message("user", user_input)
            
            # Get conversation history
            history = self.memory.get_history()
            
            # Get response from LLM
            response = self.llm.chat(history, self.system_prompt)
            
            # Add assistant response to memory
            self.memory.add_message("assistant", response)
            
            logger.info(f"Chatbot response generated")
            return response
            
        except Exception as e:
            logger.error(f"Chat error: {str(e)}")
            raise AIError(f"Failed to generate response: {str(e)}")
    
    def get_history(self):
        """Get conversation history"""
        return self.memory.get_all()
    
    def clear_history(self):
        """Clear conversation history"""
        self.memory.clear()
        logger.info("Conversation history cleared")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get chatbot statistics"""
        stats = self.memory.get_stats()
        stats["name"] = self.name
        return stats
    
    def set_system_prompt(self, prompt: str):
        """Update system prompt"""
        self.system_prompt = prompt
        logger.info("System prompt updated")
