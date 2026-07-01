"""
Configuration management for AI Powerhouse
"""
import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings"""
    
    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4")
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    llm_max_tokens: int = int(os.getenv("LLM_MAX_TOKENS", "2000"))
    
    # Application Configuration
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    app_name: str = os.getenv("APP_NAME", "AI Powerhouse")
    
    # Database Configuration
    db_url: str = os.getenv("DB_URL", "sqlite:///./ai_powerhouse.db")
    
    # Agent Configuration
    agent_max_iterations: int = int(os.getenv("AGENT_MAX_ITERATIONS", "10"))
    agent_timeout: int = int(os.getenv("AGENT_TIMEOUT", "300"))
    
    # Chatbot Configuration
    chatbot_memory_size: int = int(os.getenv("CHATBOT_MEMORY_SIZE", "10"))
    chatbot_context_window: int = int(os.getenv("CHATBOT_CONTEXT_WINDOW", "5"))
    
    # Code Generator Configuration
    code_gen_timeout: int = int(os.getenv("CODE_GEN_TIMEOUT", "30"))
    code_gen_sandbox: bool = os.getenv("CODE_GEN_SANDBOX", "True").lower() == "true"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
