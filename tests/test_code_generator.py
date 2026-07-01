"""Tests for code generator module"""
import pytest
from code_generator.generator import CodeGenerator
from code_generator.validator import CodeValidator


def test_code_generator_initialization():
    """Test code generator initialization"""
    gen = CodeGenerator()
    assert gen.llm is not None
    assert len(gen.generation_history) == 0


def test_code_validator_python_syntax():
    """Test Python code validation"""
    validator = CodeValidator()
    
    # Valid code
    valid_code = "x = 2 + 2"
    is_valid, issues = validator.validate_python(valid_code)
    assert is_valid
    assert len(issues) == 0
    
    # Invalid code
    invalid_code = "x = 2 +"
    is_valid, issues = validator.validate_python(invalid_code)
    assert not is_valid
    assert len(issues) > 0


def test_code_security_check():
    """Test code security checks"""
    validator = CodeValidator()
    
    # Safe code
    safe_code = "x = 2 + 2"
    is_safe, issues = validator.check_security(safe_code)
    assert is_safe
    
    # Dangerous code
    dangerous_code = "os.system('rm -rf /')"
    is_safe, issues = validator.check_security(dangerous_code)
    assert not is_safe
    assert len(issues) > 0


def test_code_quality_metrics():
    """Test code quality metrics"""
    validator = CodeValidator()
    
    code = """# This is a comment
def hello():
    \"\"\"Say hello\"\"\"
    print("Hello")"""
    
    metrics = validator.check_quality(code)
    assert metrics["has_comments"]
    assert metrics["has_docstrings"]
    assert metrics["lines_of_code"] > 0
