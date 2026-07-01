"""Example: Using the Code Generator"""
from code_generator.generator import CodeGenerator
from code_generator.validator import CodeValidator
from code_generator.executor import CodeExecutor
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Run code generator example"""
    logger.info("=" * 50)
    logger.info("AI Powerhouse - Code Generator Example")
    logger.info("=" * 50)
    
    # Initialize components
    generator = CodeGenerator()
    validator = CodeValidator()
    executor = CodeExecutor()
    
    # Example code generation requests
    prompts = [
        ("Create a function that calculates Fibonacci numbers", "python"),
        ("Create a function to check if a number is prime", "python"),
    ]
    
    for description, language in prompts:
        logger.info(f"\nGenerating {language} code: {description}")
        
        try:
            # Generate code
            result = generator.generate(description, language=language)
            code = result["code"]
            
            logger.info(f"\nGenerated Code:")
            logger.info(f"""```{language}
{code}
```""")
            
            # Validate code
            if language == "python":
                is_valid, issues = validator.validate_python(code)
                logger.info(f"\nValidation: {'✓ Valid' if is_valid else '✗ Invalid'}")
                if issues:
                    for issue in issues:
                        logger.warning(f"  - {issue['message']}")
                
                # Check security
                is_safe, security_issues = validator.check_security(code)
                logger.info(f"Security: {'✓ Safe' if is_safe else '⚠ Warning'}")
                if security_issues:
                    for issue in security_issues:
                        logger.warning(f"  - {issue['message']}")
                
                # Check quality
                metrics = validator.check_quality(code)
                logger.info(f"Quality Metrics:")
                for key, value in metrics.items():
                    logger.info(f"  - {key}: {value}")
                
                # Execute code (if safe)
                if is_safe and is_valid:
                    logger.info(f"\nExecuting code...")
                    exec_result = executor.execute(code, language)
                    logger.info(f"Status: {exec_result['status']}")
                    if exec_result['output']:
                        logger.info(f"Output:\n{exec_result['output']}")
                    if exec_result['error']:
                        logger.error(f"Error:\n{exec_result['error']}")
        except Exception as e:
            logger.error(f"Error: {str(e)}")
    
    # Print generation history
    logger.info(f"\nGeneration History:")
    history = generator.get_history()
    logger.info(f"Total generated: {len(history)}")


if __name__ == "__main__":
    main()
