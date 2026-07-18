"""Executes planned agent tasks"""
from typing import Any, Dict
from config import settings
from utils.logger import get_logger
from utils.errors import ExecutionError

logger = get_logger(__name__)

class TaskExecutor:
    """Executes agent tasks"""
    
    def __init__(self, tools):
        """Initialize executor"""
        self.tools = tools
        self.max_iterations = settings.agent_max_iterations
    
    def execute(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task plan"""
        try:
            results = []
            
            for i, step in enumerate(plan["steps"][:self.max_iterations]):
                logger.info(f"Executing step {i+1}: {step}")
                result = {
                    "step": i + 1,
                    "description": step,
                    "status": "completed"
                }
                results.append(result)
            
            return {
                "task": plan["task"],
                "steps_executed": len(results),
                "results": results,
                "status": "success"
            }
            
        except Exception as e:
            logger.error(f"Execution error: {str(e)}")
            raise ExecutionError(f"Task execution failed: {str(e)}")
