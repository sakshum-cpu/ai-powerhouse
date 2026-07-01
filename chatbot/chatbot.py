"""Main chatbot implementation"""
from typing import Optional
from chatbot.memory import ConversationMemory
from utils.llm import get_llm_manager
from utils.logger import get_logger
from utils.errors import ChatbotError

logger = get_logger(__name__)


class Chatbot:
    """Intelligent conversational chatbot"""
    
    def __init__(
        self,
        name: str = "AI Assistant",
        system_prompt: Optional[str] = None,
    ):
        """Initialize chatbot
        
        Args:
            name: Chatbot name
            system_prompt: Custom system prompt
        """
        self.name = name
        self.system_prompt = system_prompt or self._get_default_system_prompt()
        self.memory = ConversationMemory()
        self.llm = get_llm_manager()
        logger.info(f"Initialized chatbot: {name}")
    
    def _get_default_system_prompt(self) -> str:
        """Get default system prompt
        
        Returns:
            Default system prompt
        """
        return (
            "You are a helpful, intelligent AI assistant. "
            "Provide clear, concise, and accurate responses. "
            "If you're unsure about something, say so."
        )
    
    def chat(self, user_input: str) -> str:
        """Process user input and generate response
        
        Args:
            user_input: User's message
            
        Returns:
            Chatbot's response
            
        Raises:
            ChatbotError: If chat processing fails
        """
        try:
            # Add user message to memory
            self.memory.add_message("user", user_input)
            logger.debug(f"User: {user_input}")
            
            # Get conversation history
            messages = self.memory.get_messages()
            
            # Add system prompt as first message if not present
            if not messages or messages[0]["role"] != "system":
                messages.insert(0, {
                    "role": "system",
                    "content": self.system_prompt,
                })
            
            # Generate response
            response = self.llm.chat(messages)
            
            # Add assistant message to memory
            self.memory.add_message("assistant", response)
            logger.debug(f"Assistant: {response}")
            
            return response
        except Exception as e:
            raise ChatbotError(f"Chat processing failed: {str(e)}")
    
    def set_system_prompt(self, prompt: str) -> None:
        """Update system prompt
        
        Args:
            prompt: New system prompt
        """
        self.system_prompt = prompt
        logger.info("System prompt updated")
    
    def clear_history(self) -> None:
        """Clear conversation history"""
        self.memory.clear()
        logger.info("Conversation history cleared")
    
    def get_history(self) -> list:
        """Get conversation history
        
        Returns:
            List of messages
        """
        return self.memory.get_messages()
    
    def get_stats(self) -> dict:
        """Get chatbot statistics
        
        Returns:
            Dictionary with stats
        """
        stats = self.memory.get_summary()
        stats["name"] = self.name
        return stats
