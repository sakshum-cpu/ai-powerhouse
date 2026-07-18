"""Tool registry for agents"""
import math
from typing import Callable, Dict, Any
from utils.logger import get_logger

logger = get_logger(__name__)

class ToolRegistry:
    """Registry for agent tools"""
    
    def __init__(self):
        """Initialize tool registry"""
        self.tools = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default tools"""
        self.register("calculate", self._calculate, "Perform mathematical calculations")
        self.register("is_prime", self._is_prime, "Check if a number is prime")
        self.register("factorial", self._factorial, "Calculate factorial of a number")
        self.register("random_numbers", self._random_numbers, "Generate random numbers")
    
    def register(self, name: str, func: Callable, description: str):
        """Register a tool"""
        self.tools[name] = {
            "function": func,
            "description": description
        }
        logger.info(f"Tool registered: {name}")
    
    def execute(self, tool_name: str, *args, **kwargs) -> Any:
        """Execute a tool"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        try:
            result = self.tools[tool_name]["function"](*args, **kwargs)
            logger.info(f"Tool executed: {tool_name}")
            return result
        except Exception as e:
            logger.error(f"Tool execution error: {str(e)}")
            raise
    
    def get_tools(self):
        """Get all registered tools"""
        return {k: v["description"] for k, v in self.tools.items()}
    
    # Default tools
    @staticmethod
    def _calculate(expression):
        """Calculate mathematical expression"""
        try:
            return eval(str(expression), {"__builtins__": {}}, {})
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def _is_prime(n):
        """Check if number is prime"""
        n = int(n)
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def _factorial(n):
        """Calculate factorial"""
        return math.factorial(int(n))
    
    @staticmethod
    def _random_numbers(count, max_val=100):
        """Generate random numbers"""
        import random
        return [random.randint(1, max_val) for _ in range(int(count))]
