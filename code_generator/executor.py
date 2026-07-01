"""Safe code execution"""
from typing import Optional, Dict, Any
import subprocess
import tempfile
import os
from utils.logger import get_logger
from utils.errors import CodeExecutionError
from config import settings

logger = get_logger(__name__)


class CodeExecutor:
    """Executes generated code safely"""
    
    LANGUAGE_COMMANDS = {
        "python": "python",
        "javascript": "node",
        "java": "java",
        "go": "go run",
        "rust": "rustc",
    }
    
    LANGUAGE_EXTENSIONS = {
        "python": ".py",
        "javascript": ".js",
        "java": ".java",
        "go": ".go",
        "rust": ".rs",
    }
    
    def __init__(self, sandbox: bool = True):
        """Initialize code executor
        
        Args:
            sandbox: Whether to use sandbox (limited by timeout)
        """
        self.sandbox = sandbox
        self.timeout = settings.code_gen_timeout
    
    def execute(
        self,
        code: str,
        language: str = "python",
    ) -> Dict[str, Any]:
        """Execute code safely
        
        Args:
            code: Code to execute
            language: Programming language
            
        Returns:
            Execution result with output/errors
            
        Raises:
            CodeExecutionError: If execution fails
        """
        if language not in self.LANGUAGE_COMMANDS:
            raise CodeExecutionError(f"Unsupported language: {language}")
        
        try:
            result = {
                "language": language,
                "code": code,
                "output": "",
                "error": "",
                "status": "unknown",
            }
            
            # Create temporary file
            ext = self.LANGUAGE_EXTENSIONS[language]
            with tempfile.NamedTemporaryFile(mode='w', suffix=ext, delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                # Build command
                cmd = f"{self.LANGUAGE_COMMANDS[language]} {temp_file}"
                
                # Execute with timeout
                process = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                )
                
                result["output"] = process.stdout
                result["error"] = process.stderr
                result["status"] = "success" if process.returncode == 0 else "failed"
                
                logger.info(f"Code executed: {language} - Status: {result['status']}")
                return result
            finally:
                # Clean up temp file
                os.unlink(temp_file)
        except subprocess.TimeoutExpired:
            raise CodeExecutionError(f"Code execution timeout (>{self.timeout}s)")
        except Exception as e:
            raise CodeExecutionError(f"Code execution failed: {str(e)}")
