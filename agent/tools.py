"""Tool definitions and registry for autonomous agent"""
from typing import Callable, Dict, Any, Optional, List
from dataclasses import dataclass
from utils.logger import get_logger
from utils.errors import ToolError

logger = get_logger(__name__)


@dataclass
class Tool:
    """Tool definition"""
    name: str
    description: str
    func: Callable
    args_schema: Optional[Dict[str, Any]] = None


class ToolRegistry:
    """Registry for managing agent tools"""
    
    def __init__(self):
        """Initialize tool registry"""
        self.tools: Dict[str, Tool] = {}
        self._register_default_tools()
    
    def _register_default_tools(self) -> None:
        """Register default tools"""
        # Calculator tool
        self.register(
            "calculator",
            "Performs mathematical calculations",
            self._calculator,
            {"expression": "A mathematical expression"}
        )
        
        # Web search tool (mock)
        self.register(
            "web_search",
            "Searches the web for information",
            self._web_search,
            {"query": "Search query"}
        )
    
    def register(
        self,
        name: str,
        description: str,
        func: Callable,
        args_schema: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Register a new tool
        
        Args:
            name: Tool name
            description: Tool description
            func: Function to execute
            args_schema: Function arguments schema
        """
        tool = Tool(
            name=name,
            description=description,
            func=func,
            args_schema=args_schema or {},
        )
        self.tools[name] = tool
        logger.info(f"Registered tool: {name}")
    
    def execute(
        self,
        tool_name: str,
        **kwargs
    ) -> Any:
        """Execute a tool
        
        Args:
            tool_name: Name of tool to execute
            **kwargs: Tool arguments
            
        Returns:
            Tool result
            
        Raises:
            ToolError: If tool execution fails
        """
        if tool_name not in self.tools:
            raise ToolError(f"Tool not found: {tool_name}")
        
        try:
            tool = self.tools[tool_name]
            result = tool.func(**kwargs)
            logger.info(f"Tool executed: {tool_name}")
            return result
        except Exception as e:
            raise ToolError(f"Tool execution failed: {str(e)}")
    
    def get_tools(self) -> List[Dict[str, Any]]:
        """Get all available tools
        
        Returns:
            List of tool definitions
        """
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "args": tool.args_schema,
            }
            for tool in self.tools.values()
        ]
    
    @staticmethod
    def _calculator(expression: str) -> str:
        """Simple calculator tool
        
        Args:
            expression: Mathematical expression
            
        Returns:
            Calculation result
        """
        try:
            result = eval(expression)
            return f"Result: {result}"
        except Exception as e:
            return f"Calculation error: {str(e)}"
    
    @staticmethod
    def _web_search(query: str) -> str:
        """Mock web search tool
        
        Args:
            query: Search query
            
        Returns:
            Mock search results
        """
        return f"Search results for: {query} (Mock results)"
