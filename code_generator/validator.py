"""Code validation for code generator"""
import ast
from typing import Dict, Any
from utils.logger import get_logger
from utils.errors import ValidationError, SecurityError

logger = get_logger(__name__)

class CodeValidator:
    """Validates generated code"""
    
    def __init__(self):
        """Initialize validator"""
        self.dangerous_imports = {"os", "subprocess", "sys", "socket", "requests"}
        self.dangerous_functions = {"eval", "exec", "compile", "__import__"}
    
    def validate_python(self, code: str) -> Dict[str, Any]:
        """Validate Python code"""
        try:
            ast.parse(code)
            logger.info("Python code validation passed")
            return {"valid": True, "errors": []}
        except SyntaxError as e:
            logger.error(f"Syntax error: {str(e)}")
            return {
                "valid": False,
                "errors": [f"Syntax error: {str(e)}"]
            }
    
    def check_security(self, code: str) -> Dict[str, Any]:
        """Check code for security issues"""
        issues = []
        
        # Check for dangerous imports
        for imp in self.dangerous_imports:
            if f"import {imp}" in code or f"from {imp}" in code:
                issues.append(f"Dangerous import: {imp}")
        
        # Check for dangerous functions
        for func in self.dangerous_functions:
            if func in code:
                issues.append(f"Dangerous function: {func}")
        
        if issues:
            logger.warning(f"Security issues found: {issues}")
        
        return {
            "secure": len(issues) == 0,
            "issues": issues
        }
    
    def validate(self, code: str, language: str = "python") -> Dict[str, Any]:
        """Full validation"""
        if language == "python":
            syntax_check = self.validate_python(code)
            security_check = self.check_security(code)
            
            return {
                "valid": syntax_check["valid"] and security_check["secure"],
                "syntax_errors": syntax_check["errors"],
                "security_issues": security_check["issues"]
            }
        
        return {"valid": True, "message": f"No validation for {language}"}
