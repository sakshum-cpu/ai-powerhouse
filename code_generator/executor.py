"""Safe code execution for code generator"""
import sys
from io import StringIO
from typing import Dict, Any
from config import settings
from utils.logger import get_logger
from utils.errors import ExecutionError, SecurityError

logger = get_logger(__name__)

class CodeExecutor:
    """Executes generated code safely"""
    
    def __init__(self):
        """Initialize executor"""
        self.timeout = settings.code_gen_timeout
        self.sandbox = settings.code_gen_sandbox
    
    def execute_python(self, code: str) -> Dict[str, Any]:
        """Execute Python code safely"""
        try:
            # Capture output
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            # Create safe environment
            safe_dict = {
                "__builtins__": {
                    "print": print,
                    "len": len,
                    "range": range,
                    "list": list,
                    "dict": dict,
                    "str": str,
                    "int": int,
                    "float": float,
                    "sum": sum,
                    "max": max,
                    "min": min,
                }
            }
            
            # Execute code
            exec(code, safe_dict)
            
            # Get output
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            logger.info("Code executed successfully")
            return {
                "success": True,
                "output": output,
                "error": None
            }
            
        except Exception as e:
            sys.stdout = old_stdout
            logger.error(f"Execution error: {str(e)}")
            return {
                "success": False,
                "output": "",
                "error": str(e)
            }
    
    def execute(self, code: str, language: str = "python") -> Dict[str, Any]:
        """Execute code"""
        if language == "python":
            return self.execute_python(code)
        
        return {
            "success": False,
            "error": f"Execution not supported for {language}"
        }
