"""Code Generator implementation"""
from typing import Dict, Any, Optional
from code_generator.validator import CodeValidator
from code_generator.executor import CodeExecutor
from utils.llm import get_llm
from utils.logger import get_logger
from utils.errors import AIError

logger = get_logger(__name__)

class CodeGenerator:
    """Generates and executes code"""
    
    def __init__(self):
        """Initialize code generator"""
        self.llm = get_llm()
        self.validator = CodeValidator()
        self.executor = CodeExecutor()
        self.history = []
        logger.info("Code Generator initialized")
    
    def generate(self, description: str, language: str = "python") -> Dict[str, Any]:
        """Generate code from description"""
        try:
            prompt = f"""
Generate clean, well-commented {language} code for the following:
{description}

Provide only the code, no explanations.
            """
            
            code = self.llm.generate(prompt)
            
            # Validate code
            validation = self.validator.validate(code, language)
            
            result = {
                "description": description,
                "language": language,
                "code": code,
                "valid": validation["valid"],
                "validation": validation
            }
            
            self.history.append(result)
            logger.info(f"Code generated for: {description[:50]}...")
            
            return result
            
        except Exception as e:
            logger.error(f"Code generation error: {str(e)}")
            raise AIError(f"Failed to generate code: {str(e)}")
    
    def generate_and_execute(self, description: str, language: str = "python") -> Dict[str, Any]:
        """Generate and execute code"""
        try:
            # Generate code
            result = self.generate(description, language)
            
            if result["valid"]:
                # Execute code
                execution = self.executor.execute(result["code"], language)
                result["execution"] = execution
            else:
                result["execution"] = {"success": False, "error": "Code validation failed"}
            
            return result
            
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
    
    def generate_explanation(self, code: str) -> str:
        """Generate explanation for code"""
        prompt = f"Explain this code in simple terms:\n{code}"
        return self.llm.generate(prompt)
    
    def get_history(self):
        """Get generation history"""
        return self.history
