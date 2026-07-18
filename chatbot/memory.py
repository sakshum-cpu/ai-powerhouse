"""Memory management for chatbot"""
from typing import List, Dict
from datetime import datetime
from config import settings

class Memory:
    """Manages conversation memory"""
    
    def __init__(self, max_size=None):
        """Initialize memory"""
        self.max_size = max_size or settings.chatbot_memory_size
        self.messages = []
        self.metadata = {}
    
    def add_message(self, role, content, metadata=None):
        """Add message to memory"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.messages.append(message)
        
        # Keep only recent messages
        if len(self.messages) > self.max_size:
            self.messages.pop(0)
    
    def get_history(self, window_size=None):
        """Get message history"""
        size = window_size or settings.chatbot_context_window
        return self.messages[-size:]
    
    def get_all(self):
        """Get all messages"""
        return self.messages
    
    def clear(self):
        """Clear memory"""
        self.messages = []
    
    def get_stats(self):
        """Get memory statistics"""
        return {
            "total_messages": len(self.messages),
            "user_messages": len([m for m in self.messages if m["role"] == "user"]),
            "assistant_messages": len([m for m in self.messages if m["role"] == "assistant"]),
            "memory_size": self.max_size
        }
