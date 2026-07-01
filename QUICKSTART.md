# 🚀 Quick Start Guide

Get AI Powerhouse running in 5 minutes!

## Prerequisites

- Python 3.10 or higher
- OpenAI API key (you already provided it ✅)
- Git (optional, for cloning)

## Installation (2 minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/sakshum-cpu/ai-powerhouse.git
cd ai-powerhouse
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Done!** Your environment is ready. ✅

---

## Run Setup & Tests (2 minutes)

### Verify Everything Works
```bash
python setup_and_test.py
```

This script will:
- ✅ Test the Chatbot (multi-turn conversations)
- ✅ Test the Agent (task execution)
- ✅ Test the Code Generator (code creation & validation)

**Expected Output:**
```
============================================================
  🚀 AI POWERHOUSE - SETUP & TEST SUITE
============================================================

Configuration:
  - App Name: AI Powerhouse
  - LLM Model: gpt-4
  - Temperature: 0.7
  - Debug Mode: True

...test results...

✅ Chatbot: Chatbot working perfectly! ✅
✅ Agent: Agent working perfectly! ✅
✅ Code Generator: Code Generator working perfectly! ✅

🎉 ALL TESTS PASSED! Your AI Powerhouse is ready! 🚀
```

---

## Run Examples (1 minute each)

### Example 1: Interactive Chatbot
```bash
python examples/chatbot_example.py
```
**What it does:** 
- Demonstrates multi-turn conversation
- Shows conversation memory in action
- Displays conversation statistics

### Example 2: Autonomous Agent
```bash
python examples/agent_example.py
```
**What it does:**
- Creates a task plan
- Executes multiple tasks
- Shows available tools

### Example 3: Code Generator
```bash
python examples/code_gen_example.py
```
**What it does:**
- Generates Python code from descriptions
- Validates syntax and security
- Shows quality metrics

---

## Use It in Your Code

### 💬 Use the Chatbot
```python
from chatbot.chatbot import Chatbot

# Create chatbot
bot = Chatbot(name="MyAssistant")

# Chat with it
response = bot.chat("Tell me about Python")
print(response)

# Clear history when done
bot.clear_history()
```

### 🤖 Use the Agent
```python
from agent.agent import Agent

# Create agent
agent = Agent(name="TaskBot")

# Execute task
result = agent.execute_task("Calculate 50 * 20 and explain the result")
print(result["final_result"])

# View execution history
history = agent.get_history()
print(f"Executed {len(history)} tasks")
```

### 🧠 Use the Code Generator
```python
from code_generator.generator import CodeGenerator
from code_generator.validator import CodeValidator

# Create generator and validator
gen = CodeGenerator()
validator = CodeValidator()

# Generate code
result = gen.generate("Create a function that sorts a list", language="python")
code = result["code"]

# Validate it
is_valid, issues = validator.validate_python(code)
print(f"Valid: {is_valid}")
print(f"Code:\n{code}")
```

---

## Run Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_chatbot.py

# Verbose output
pytest tests/ -v

# Stop on first failure
pytest tests/ -x
```

---

## Project Structure

```
ai-powerhouse/
├── chatbot/              # Conversation engine
│   ├── chatbot.py
│   └── memory.py
├── agent/                # Task execution engine
│   ├── agent.py
│   ├── tools.py
│   └── planner.py
├── code_generator/       # Code generation
│   ├── generator.py
│   ├── validator.py
│   └── executor.py
├── utils/                # Utilities
│   ├── llm.py
│   ├── logger.py
│   └── errors.py
├── examples/             # Example scripts
│   ├── chatbot_example.py
│   ├── agent_example.py
│   └── code_gen_example.py
├── tests/                # Test suite
│   ├── test_chatbot.py
│   ├── test_agent.py
│   └── test_code_generator.py
├── docs/                 # Documentation
│   ├── API.md
│   └── ARCHITECTURE.md
├── config.py             # Configuration
├── .env                  # Environment variables (configured ✅)
├── requirements.txt      # Dependencies
└── setup_and_test.py     # Setup script
```

---

## Configuration

Edit `config.py` to customize:

```python
# LLM Settings
llm_model = "gpt-4"              # Change model
llm_temperature = 0.7             # Higher = more creative (0-1)
llm_max_tokens = 2000             # Max response length

# Application
debug = True                       # Enable debug logging
log_level = "INFO"                 # Log verbosity

# Agent
agent_max_iterations = 10          # Max task steps
agent_timeout = 300                # Max execution time (seconds)

# Chatbot
chatbot_memory_size = 10           # Messages to keep in memory
chatbot_context_window = 5         # Messages for context

# Code Generator
code_gen_timeout = 30              # Max execution time
code_gen_sandbox = True            # Run in sandbox
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError`
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: API key not working
```bash
# Check .env file has correct key
cat .env | grep OPENAI_API_KEY

# Verify key format (should start with sk-proj-)
```

### Issue: Tests failing
```bash
# Run with verbose output to see errors
pytest tests/ -v

# Check configuration
python -c "from config import settings; print(settings.llm_model)"
```

### Issue: Slow responses
```bash
# Reduce max_tokens in config.py
llm_max_tokens = 500  # Lower value = faster responses
```

---

## Next Steps

1. ✅ **Setup Complete** - You're here!
2. ✅ **Run Tests** - `python setup_and_test.py`
3. 🔄 **Try Examples** - `python examples/chatbot_example.py`
4. 🛠️ **Build Something** - Use code snippets above
5. 📖 **Read Docs** - Check `docs/API.md`
6. 🚀 **Deploy** - Share your creation!

---

## Commands Cheat Sheet

```bash
# Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run
python setup_and_test.py
python examples/chatbot_example.py
python examples/agent_example.py
python examples/code_gen_example.py

# Test
pytest tests/
pytest tests/ -v
pytest tests/test_chatbot.py

# Debug
python -c "from chatbot import Chatbot; print('OK')"
python config.py
```

---

## Support & Resources

- 📖 **API Reference**: `docs/API.md`
- 🏗️ **Architecture**: `docs/ARCHITECTURE.md`
- 🤝 **Contributing**: `CONTRIBUTING.md`
- 🐛 **Issues**: [GitHub Issues](https://github.com/sakshum-cpu/ai-powerhouse/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/sakshum-cpu/ai-powerhouse/discussions)

---

## You're All Set! 🎉

Your AI Powerhouse is ready to use. Start with:

```bash
python setup_and_test.py
```

Then run your first example:

```bash
python examples/chatbot_example.py
```

Happy coding! 🚀
