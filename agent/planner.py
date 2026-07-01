"""Task planning for autonomous agent"""
from typing import Dict, List, Any, Optional
from utils.llm import get_llm_manager
from utils.logger import get_logger
import json

logger = get_logger(__name__)


class TaskPlanner:
    """Plans tasks into executable steps"""
    
    def __init__(self):
        """Initialize task planner"""
        self.llm = get_llm_manager()
    
    def plan(
        self,
        task: str,
        available_tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Plan a task into steps
        
        Args:
            task: Task description
            available_tools: List of available tools
            
        Returns:
            Plan with steps
        """
        available_tools = available_tools or []
        
        tools_description = "\n".join([
            f"- {tool['name']}: {tool['description']}"
            for tool in available_tools
        ])
        
        prompt = f"""Plan the following task into executable steps.
        
Task: {task}

Available tools:
{tools_description}

Create a detailed plan with the following JSON format:
{{
    "goal": "Task goal",
    "steps": [
        {{
            "step_number": 1,
            "description": "Step description",
            "action": "think" or "use_tool",
            "tool": "tool_name_if_applicable",
            "args": {{}}
        }}
    ]
}}

Respond only with valid JSON."""
        
        try:
            response = self.llm.generate(prompt)
            # Extract JSON from response
            import re
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                plan = json.loads(json_match.group())
                logger.info(f"Plan created with {len(plan.get('steps', []))} steps")
                return plan
        except Exception as e:
            logger.error(f"Planning failed: {str(e)}")
        
        # Fallback plan
        return {
            "goal": task,
            "steps": [
                {
                    "step_number": 1,
                    "description": task,
                    "action": "think",
                    "prompt": task,
                }
            ]
        }
