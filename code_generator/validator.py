"""Code validation utilities"""
from typing import Dict, List, Tuple
import ast
import re
from utils.logger import get_logger

logger = get_logger(__name__)


class CodeValidator:
    """Validates generated code"""
    
    def __init__(self):
        """Initialize code validator"""
        self.issues: List[Dict[str, any]] = []
    
    def validate_python(self, code: str) -> Tuple[bool, List[Dict[str, any]]]:
        """Validate Python code syntax
        
        Args:
            code: Python code to validate
            
        Returns:
            Tuple of (is_valid, issues)
        """
        issues = []
        
        try:
            ast.parse(code)
            logger.info("Python code syntax is valid")
            return True, issues
        except SyntaxError as e:
            issues.append({
                "type": "syntax_error",
                "message": str(e),
                "line": e.lineno,
            })
            logger.warning(f"Syntax error: {e}")
            return False, issues
    
    def check_security(self, code: str) -> Tuple[bool, List[Dict[str, any]]]:
        """Check code for security issues
        
        Args:
            code: Code to check
            
        Returns:
            Tuple of (is_safe, issues)
        """
        issues = []
        dangerous_patterns = [
            (r'os\.system|subprocess\.call|exec|eval', 'Potentially dangerous system call'),
            (r'open\(.*[\'\"]w[\'\")', 'File write operation'),
            (r'import.*shell', 'Shell operation'),
        ]
        
        for pattern, description in dangerous_patterns:
            if re.search(pattern, code):
                issues.append({
                    "type": "security_warning",
                    "message": description,
                    "pattern": pattern,
                })
        
        is_safe = len(issues) == 0
        if is_safe:
            logger.info("Code passed security checks")
        else:
            logger.warning(f"Security issues found: {len(issues)}")
        
        return is_safe, issues
    
    def check_quality(self, code: str) -> Dict[str, any]:
        """Check code quality
        
        Args:
            code: Code to check
            
        Returns:
            Quality metrics
        """
        metrics = {
            "lines_of_code": len(code.split('\n')),
            "has_comments": '#' in code,
            "has_docstrings": '"""' in code or "'''" in code,
            "avg_line_length": sum(len(line) for line in code.split('\n')) / max(1, len(code.split('\n'))),
        }
        
        return metrics
