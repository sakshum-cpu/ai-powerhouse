"""Custom exceptions for AI Powerhouse"""

class AIError(Exception):
    """Base exception for AI Powerhouse"""
    pass

class LLMError(AIError):
    """LLM related errors"""
    pass

class ValidationError(AIError):
    """Validation errors"""
    pass

class ExecutionError(AIError):
    """Execution errors"""
    pass

class ConfigError(AIError):
    """Configuration errors"""
    pass

class SecurityError(AIError):
    """Security related errors"""
    pass
