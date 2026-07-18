"""LLM Manager for AI Powerhouse"""
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from config import settings
from utils.logger import get_logger
from utils.errors import LLMError, ConfigError

logger = get_logger(__name__)

class LLMManager:
    """Manages LLM interactions"""
    
    def __init__(self):
        """Initialize LLM Manager"""
        if not settings.openai_api_key:
            raise ConfigError("OPENAI_API_KEY not configured in .env")
        
        self.client = ChatOpenAI(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            max_tokens=settings.llm_max_tokens,
            api_key=settings.openai_api_key
        )
        logger.info(f"LLM initialized with model: {settings.llm_model}")
    
    def chat(self, messages, system_prompt=None):
        """Send messages to LLM"""
        try:
            formatted_messages = []
            
            if system_prompt:
                formatted_messages.append(SystemMessage(content=system_prompt))
            
            for msg in messages:
                if isinstance(msg, dict):
                    if msg.get('role') == 'user':
                        formatted_messages.append(HumanMessage(content=msg.get('content', '')))
                    elif msg.get('role') == 'assistant':
                        formatted_messages.append(AIMessage(content=msg.get('content', '')))
                else:
                    formatted_messages.append(HumanMessage(content=str(msg)))
            
            response = self.client.invoke(formatted_messages)
            logger.info("LLM response generated successfully")
            return response.content
            
        except Exception as e:
            logger.error(f"LLM error: {str(e)}")
            raise LLMError(f"Failed to get LLM response: {str(e)}")
    
    def generate(self, prompt, system_prompt=None):
        """Generate response from prompt"""
        return self.chat([{"role": "user", "content": prompt}], system_prompt)

# Global LLM instance
llm_manager = None

def get_llm():
    """Get or create LLM manager instance"""
    global llm_manager
    if llm_manager is None:
        llm_manager = LLMManager()
    return llm_manager
