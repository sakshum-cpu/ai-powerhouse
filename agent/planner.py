"""Task planning for agents"""
from typing import List, Dict, Any
from utils.llm import get_llm
from utils.logger import get_logger

logger = get_logger(__name__)

class TaskPlanner:
    """Plans task execution steps"""
    
    def __init__(self):
        """Initialize planner"""
        self.llm = get_llm()
    
    def plan(self, task: str, available_tools: List[str]) -> Dict[str, Any]:
        """Create execution plan for task"""
        tools_str = ", ".join(available_tools)
        
        prompt = f"""
Break down this task into clear, executable steps:
Task: {task}

Available tools: {tools_str}

Provide a step-by-step plan. Format each step as:
Step 1: [description]
Step 2: [description]
etc.
        """
        
        plan_text = self.llm.generate(prompt)
        
        # Parse plan
        steps = []
        for line in plan_text.split('\n'):
            if line.strip().startswith('Step'):
                steps.append(line.strip())
        
        logger.info(f"Task plan created with {len(steps)} steps")
        
        return {
            "task": task,
            "steps": steps,
            "plan_text": plan_text
        }
