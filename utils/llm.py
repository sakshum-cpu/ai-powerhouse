"""LLM interaction utilities"""
from typing import Optional, List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from config import settings
from utils.logger import get_logger
from utils.errors import LLMError

logger = get_logger(__name__)


class LLMManager:
    """Manages LLM interactions"""
    
    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ):
        """Initialize LLM Manager
        
        Args:
            model: LLM model name
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
        """
        self.model_name = model or settings.llm_model
        self.temperature = temperature if temperature is not None else settings.llm_temperature
        self.max_tokens = max_tokens or settings.llm_max_tokens
        
        try:
            self.llm = ChatOpenAI(
                api_key=settings.openai_api_key,
                model_name=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
        except Exception as e:
            raise LLMError(f"Failed to initialize LLM: {str(e)}")
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """Generate text using LLM
        
        Args:
            prompt: User prompt
            system_prompt: System prompt for context
            
        Returns:
            Generated text
        """
        try:
            messages = []
            
            if system_prompt:
                messages.append(SystemMessage(content=system_prompt))
            
            messages.append(HumanMessage(content=prompt))
            
            response = self.llm(messages)
            return response.content
        except Exception as e:
            raise LLMError(f"Failed to generate text: {str(e)}")
    
    def chat(
        self,
        messages: List[Dict[str, str]],
    ) -> str:
        """Chat with LLM using message history
        
        Args:
            messages: List of messages with 'role' and 'content'
            
        Returns:
            Generated response
        """
        try:
            formatted_messages = []
            
            for msg in messages:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                
                if role == "system":
                    formatted_messages.append(SystemMessage(content=content))
                elif role == "assistant":
                    formatted_messages.append(AIMessage(content=content))
                else:
                    formatted_messages.append(HumanMessage(content=content))
            
            response = self.llm(formatted_messages)
            return response.content
        except Exception as e:
            raise LLMError(f"Chat failed: {str(e)}")
    
    def set_model(self, model: str) -> None:
        """Switch to a different model
        
        Args:
            model: Model name
        """
        self.model_name = model
        self.llm.model_name = model
        logger.info(f"Switched to model: {model}")


# Global LLM manager instance
_llm_manager: Optional[LLMManager] = None


def get_llm_manager() -> LLMManager:
    """Get or create global LLM manager instance
    
    Returns:
        LLM manager instance
    """
    global _llm_manager
    if _llm_manager is None:
        _llm_manager = LLMManager()
    return _llm_manager
