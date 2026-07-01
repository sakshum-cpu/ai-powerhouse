"""Code generation functionality"""
from typing import Optional, Dict, Any
from utils.llm import get_llm_manager
from utils.logger import get_logger
from utils.errors import CodeExecutionError

logger = get_logger(__name__)


class CodeGenerator:
    """Generates code from natural language descriptions"""
    
    LANGUAGE_PROMPTS = {
        "python": "Generate Python code that",
        "javascript": "Generate JavaScript code that",
        "java": "Generate Java code that",
        "go": "Generate Go code that",
        "rust": "Generate Rust code that",
    }
    
    def __init__(self):
        """Initialize code generator"""
        self.llm = get_llm_manager()
        self.generation_history = []
    
    def generate(
        self,
        description: str,
        language: str = "python",
        requirements: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate code from description
        
        Args:
            description: What the code should do
            language: Programming language (default: python)
            requirements: Additional requirements
            
        Returns:
            Generated code with metadata
            
        Raises:
            CodeExecutionError: If generation fails
        """
        try:
            language = language.lower()
            if language not in self.LANGUAGE_PROMPTS:
                raise CodeExecutionError(f"Unsupported language: {language}")
            
            prompt = self._build_prompt(description, language, requirements)
            code = self.llm.generate(prompt)
            
            # Clean code (remove markdown if present)
            code = self._clean_code(code, language)
            
            result = {
                "language": language,
                "description": description,
                "code": code,
                "requirements": requirements,
            }
            
            self.generation_history.append(result)
            logger.info(f"Generated {language} code")
            return result
        except Exception as e:
            raise CodeExecutionError(f"Code generation failed: {str(e)}")
    
    def _build_prompt(
        self,
        description: str,
        language: str,
        requirements: Optional[str] = None,
    ) -> str:
        """Build generation prompt
        
        Args:
            description: Code description
            language: Target language
            requirements: Additional requirements
            
        Returns:
            Generation prompt
        """
        prompt = f"{self.LANGUAGE_PROMPTS[language]} {description}"
        
        if requirements:
            prompt += f"\n\nRequirements:\n{requirements}"
        
        prompt += f"\n\nProvide clean, well-commented {language} code. Include docstrings/comments."
        
        return prompt
    
    @staticmethod
    def _clean_code(code: str, language: str) -> str:
        """Clean generated code
        
        Args:
            code: Raw generated code
            language: Programming language
            
        Returns:
            Cleaned code
        """
        # Remove markdown code blocks if present
        if f"```{language}" in code:
            start = code.find(f"```{language}") + len(f"```{language}")
            end = code.rfind("```")
            code = code[start:end].strip()
        elif "```" in code:
            start = code.find("```") + 3
            end = code.rfind("```")
            code = code[start:end].strip()
        
        return code.strip()
    
    def generate_explanation(
        self,
        code: str,
        language: str = "python",
    ) -> str:
        """Generate explanation for code
        
        Args:
            code: Code to explain
            language: Programming language
            
        Returns:
            Code explanation
        """
        prompt = f"""Explain the following {language} code in simple terms:
        
{code}

Provide a clear, concise explanation of what this code does."""
        
        return self.llm.generate(prompt)
    
    def get_history(self) -> list:
        """Get generation history
        
        Returns:
            List of generated code
        """
        return self.generation_history
