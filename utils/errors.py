"""Custom exceptions for AI Powerhouse"""


class AIError(Exception):
    """Base exception for all AI Powerhouse errors"""
    pass


class LLMError(AIError):
    """Raised when LLM interaction fails"""
    pass


class AgentError(AIError):
    """Raised when agent execution fails"""
    pass


class CodeExecutionError(AIError):
    """Raised when code execution fails"""
    pass


class ChatbotError(AIError):
    """Raised when chatbot operation fails"""
    pass


class ToolError(AgentError):
    """Raised when a tool execution fails"""
    pass
