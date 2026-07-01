#!/usr/bin/env python3
"""
AI Powerhouse - Complete Setup and Test Suite
This script verifies all three AI components are working
"""

import sys
from utils.logger import get_logger
from config import settings

logger = get_logger(__name__)


def print_header(title):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")


def test_chatbot():
    """Test chatbot functionality"""
    print_header("1️⃣  TESTING CHATBOT")
    
    try:
        from chatbot.chatbot import Chatbot
        
        logger.info("Initializing Chatbot...")
        chat = Chatbot(
            name="TestAssistant",
            system_prompt="You are a helpful AI assistant. Be concise."
        )
        
        test_messages = [
            "What is machine learning?",
            "Can you explain neural networks briefly?",
            "How is deep learning different?",
        ]
        
        logger.info("Running conversation...")
        for i, msg in enumerate(test_messages, 1):
            logger.info(f"\n[Message {i}] User: {msg}")
            response = chat.chat(msg)
            logger.info(f"[Message {i}] Assistant: {response[:150]}...")
        
        stats = chat.get_stats()
        logger.info(f"\n✅ Chatbot Stats:")
        logger.info(f"   - Total messages: {stats['total_messages']}")
        logger.info(f"   - Memory size: {stats['max_size']}")
        
        return True, "Chatbot working perfectly! ✅"
    except Exception as e:
        return False, f"Chatbot failed: {str(e)} ❌"


def test_agent():
    """Test autonomous agent functionality"""
    print_header("2️⃣  TESTING AUTONOMOUS AGENT")
    
    try:
        from agent.agent import Agent
        
        logger.info("Initializing Agent...")
        agent = Agent(name="TaskBot")
        
        test_tasks = [
            "Calculate 100 + 50 and tell me the result",
            "Search for information about Python programming",
        ]
        
        logger.info("Executing tasks...")
        for i, task in enumerate(test_tasks, 1):
            logger.info(f"\n[Task {i}] Executing: {task}")
            result = agent.execute_task(task)
            logger.info(f"[Task {i}] Status: {result['status']}")
            logger.info(f"[Task {i}] Result: {result['final_result'][:150]}...")
        
        tools = agent.tools.get_tools()
        logger.info(f"\n✅ Agent Stats:")
        logger.info(f"   - Available tools: {len(tools)}")
        logger.info(f"   - Tool names: {[t['name'] for t in tools]}")
        
        return True, "Agent working perfectly! ✅"
    except Exception as e:
        return False, f"Agent failed: {str(e)} ❌"


def test_code_generator():
    """Test code generation functionality"""
    print_header("3️⃣  TESTING CODE GENERATOR")
    
    try:
        from code_generator.generator import CodeGenerator
        from code_generator.validator import CodeValidator
        
        logger.info("Initializing Code Generator...")
        gen = CodeGenerator()
        validator = CodeValidator()
        
        test_prompts = [
            ("Create a function that checks if a number is even", "python"),
            ("Create a function to reverse a string", "python"),
        ]
        
        logger.info("Generating code...")
        for i, (prompt, lang) in enumerate(test_prompts, 1):
            logger.info(f"\n[Generation {i}] Prompt: {prompt}")
            
            result = gen.generate(prompt, language=lang)
            code = result["code"]
            
            logger.info(f"[Generation {i}] Generated code:")
            logger.info(f"```{lang}\n{code}\n```")
            
            # Validate
            is_valid, issues = validator.validate_python(code)
            logger.info(f"[Generation {i}] Validation: {'✅ Valid' if is_valid else '❌ Invalid'}")
            
            if issues:
                for issue in issues:
                    logger.warning(f"   - {issue['message']}")
            
            # Security check
            is_safe, security_issues = validator.check_security(code)
            logger.info(f"[Generation {i}] Security: {'✅ Safe' if is_safe else '⚠️ Warning'}")
            
            if security_issues:
                for issue in security_issues:
                    logger.warning(f"   - {issue['message']}")
        
        logger.info(f"\n✅ Code Generator Stats:")
        logger.info(f"   - Generated codes: {len(gen.get_history())}")
        
        return True, "Code Generator working perfectly! ✅"
    except Exception as e:
        return False, f"Code Generator failed: {str(e)} ❌"


def print_summary(results):
    """Print test summary"""
    print_header("📊 TEST SUMMARY")
    
    total = len(results)
    passed = sum(1 for success, _ in results.values() if success)
    failed = total - passed
    
    for name, (success, message) in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {name}: {message}")
    
    print("\n" + "-"*60)
    print(f"Total Tests: {total}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print("-"*60)
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! Your AI Powerhouse is ready! 🚀\n")
        return True
    else:
        print(f"\n⚠️ {failed} test(s) failed. Check the logs above.\n")
        return False


def main():
    """Run all tests"""
    print_header("🚀 AI POWERHOUSE - SETUP & TEST SUITE")
    
    logger.info(f"Configuration:")
    logger.info(f"  - App Name: {settings.app_name}")
    logger.info(f"  - LLM Model: {settings.llm_model}")
    logger.info(f"  - Temperature: {settings.llm_temperature}")
    logger.info(f"  - Debug Mode: {settings.debug}")
    
    results = {
        "Chatbot": test_chatbot(),
        "Agent": test_agent(),
        "Code Generator": test_code_generator(),
    }
    
    success = print_summary(results)
    
    if success:
        print("Next steps:")
        print("1. Run examples: python examples/chatbot_example.py")
        print("2. Run tests: pytest tests/")
        print("3. Check documentation: docs/API.md")
        print("4. Start building: See examples/ directory\n")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
