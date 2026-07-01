"""Autonomous agent implementation"""
from typing import Optional, Dict, Any
from agent.tools import ToolRegistry
from agent.planner import TaskPlanner
from utils.llm import get_llm_manager
from utils.logger import get_logger
from utils.errors import AgentError
from config import settings

logger = get_logger(__name__)


class Agent:
    """Autonomous task-executing agent"""
    
    def __init__(self, name: str = "Agent"):
        """Initialize agent
        
        Args:
            name: Agent name
        """
        self.name = name
        self.tools = ToolRegistry()
        self.planner = TaskPlanner()
        self.llm = get_llm_manager()
        self.execution_history = []
        logger.info(f"Initialized agent: {name}")
    
    def execute_task(self, task: str) -> Dict[str, Any]:
        """Execute a task
        
        Args:
            task: Task description
            
        Returns:
            Execution result
            
        Raises:
            AgentError: If task execution fails
        """
        try:
            logger.info(f"Executing task: {task}")
            
            # Plan task
            plan = self.planner.plan(task, self.tools.get_tools())
            
            result = {
                "task": task,
                "plan": plan,
                "steps_executed": [],
                "final_result": None,
                "status": "pending",
            }
            
            # Execute plan steps
            for i, step in enumerate(plan.get("steps", [])):
                if i >= settings.agent_max_iterations:
                    logger.warning("Max iterations reached")
                    break
                
                try:
                    step_result = self._execute_step(step)
                    result["steps_executed"].append({
                        "step": step,
                        "result": step_result,
                    })
                except Exception as e:
                    logger.error(f"Step failed: {str(e)}")
                    result["steps_executed"].append({
                        "step": step,
                        "error": str(e),
                    })
            
            result["final_result"] = self._synthesize_result(result)
            result["status"] = "completed"
            
            self.execution_history.append(result)
            return result
        except Exception as e:
            raise AgentError(f"Task execution failed: {str(e)}")
    
    def _execute_step(self, step: Dict[str, Any]) -> str:
        """Execute a single step
        
        Args:
            step: Step definition
            
        Returns:
            Step result
        """
        action = step.get("action")
        tool_name = step.get("tool")
        args = step.get("args", {})
        
        if action == "think":
            prompt = step.get("prompt", "")
            return self.llm.generate(prompt)
        elif action == "use_tool" and tool_name:
            return self.tools.execute(tool_name, **args)
        else:
            return "Step completed"
    
    def _synthesize_result(self, result: Dict[str, Any]) -> str:
        """Synthesize final result from execution steps
        
        Args:
            result: Execution result dict
            
        Returns:
            Synthesized final result
        """
        steps_info = "\n".join([
            f"Step {i+1}: {s.get('step', {}).get('description', 'Unknown')}\n"
            f"Result: {s.get('result', s.get('error', 'Unknown'))}\n"
            for i, s in enumerate(result["steps_executed"])
        ])
        
        prompt = f"""Based on the following execution steps, provide a concise final summary:\n{steps_info}"""
        
        return self.llm.generate(prompt)
    
    def add_tool(self, name: str, description: str, func: callable) -> None:
        """Add a custom tool
        
        Args:
            name: Tool name
            description: Tool description
            func: Tool function
        """
        self.tools.register(name, description, func)
        logger.info(f"Added custom tool: {name}")
    
    def get_history(self) -> list:
        """Get execution history
        
        Returns:
            List of past executions
        """
        return self.execution_history
