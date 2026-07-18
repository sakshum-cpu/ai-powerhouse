"""Autonomous Agent implementation"""
from typing import Optional, Dict, Any
from agent.tools import ToolRegistry
from agent.planner import TaskPlanner
from agent.executor import TaskExecutor
from utils.logger import get_logger
from utils.errors import AIError

logger = get_logger(__name__)

class Agent:
    """Autonomous agent for task execution"""
    
    def __init__(self, name="TaskMaster"):
        """Initialize agent"""
        self.name = name
        self.tools = ToolRegistry()
        self.planner = TaskPlanner()
        self.executor = TaskExecutor(self.tools)
        self.execution_history = []
        logger.info(f"Agent '{name}' initialized")
    
    def execute_task(self, task: str) -> Dict[str, Any]:
        """Execute a complex task"""
        try:
            logger.info(f"Executing task: {task}")
            
            # Plan task
            available_tools = list(self.tools.get_tools().keys())
            plan = self.planner.plan(task, available_tools)
            
            # Execute plan
            result = self.executor.execute(plan)
            
            # Store in history
            self.execution_history.append({
                "task": task,
                "plan": plan,
                "result": result
            })
            
            logger.info(f"Task completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Task execution error: {str(e)}")
            raise AIError(f"Failed to execute task: {str(e)}")
    
    def add_tool(self, name: str, func, description: str):
        """Add custom tool"""
        self.tools.register(name, func, description)
        logger.info(f"Custom tool added: {name}")
    
    def get_history(self):
        """Get execution history"""
        return self.execution_history
    
    def get_available_tools(self):
        """Get available tools"""
        return self.tools.get_tools()
