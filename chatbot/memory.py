"""Conversation memory management for chatbot"""
from typing import List, Dict, Optional
from datetime import datetime
from config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class ConversationMemory:
    """Manages conversation history and context"""
    
    def __init__(self, max_size: Optional[int] = None):
        """Initialize conversation memory
        
        Args:
            max_size: Maximum number of messages to keep
        """
        self.max_size = max_size or settings.chatbot_memory_size
        self.messages: List[Dict[str, any]] = []
    
    def add_message(self, role: str, content: str) -> None:
        """Add a message to memory
        
        Args:
            role: 'user', 'assistant', or 'system'
            content: Message content
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        }
        self.messages.append(message)
        
        # Remove oldest messages if exceeding max size
        if len(self.messages) > self.max_size:
            removed = self.messages.pop(0)
            logger.debug(f"Removed oldest message: {removed['role']} at {removed['timestamp']}")
    
    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages in memory
        
        Returns:
            List of messages
        """
        return [{
            "role": msg["role"],
            "content": msg["content"],
        } for msg in self.messages]
    
    def get_context(self, window_size: Optional[int] = None) -> str:
        """Get recent conversation context
        
        Args:
            window_size: Number of recent messages to include
            
        Returns:
            Formatted context string
        """
        window = window_size or settings.chatbot_context_window
        recent_messages = self.messages[-window:]
        
        context = ""
        for msg in recent_messages:
            role = msg["role"].upper()
            content = msg["content"]
            context += f"{role}: {content}\n"
        
        return context
    
    def clear(self) -> None:
        """Clear all messages from memory"""
        self.messages.clear()
        logger.info("Conversation memory cleared")
    
    def get_summary(self) -> Dict[str, any]:
        """Get memory statistics
        
        Returns:
            Dictionary with memory stats
        """
        return {
            "total_messages": len(self.messages),
            "max_size": self.max_size,
            "first_message_time": self.messages[0]["timestamp"] if self.messages else None,
            "last_message_time": self.messages[-1]["timestamp"] if self.messages else None,
        }
