# 🧠⚡ NEURON - AI Powerhouse

**Your Ultimate AI System: Intelligent Conversations, Autonomous Task Execution & Code Generation**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

---

## 🚀 What is NEURON?

**NEURON** is a production-ready AI system combining three powerful capabilities:

- 💬 **Chatbot** - Multi-turn conversations with context management
- 🤖 **Autonomous Agent** - Intelligent task planning and execution
- 🧠 **Code Generator** - AI-powered code creation, validation & execution

Think of NEURON as your personal AI assistant that can chat, think, plan, execute tasks, AND write code - all in one powerful system!

---

## ✨ Key Features

### 🎯 Intelligent Chatbot
- Multi-turn conversations with memory
- Context-aware responses
- Custom system prompts
- Conversation tracking & statistics

### 🔧 Autonomous Agent
- Automatic task planning & decomposition
- Tool orchestration (extensible)
- Step-by-step execution
- Result synthesis & analysis

### 💻 Code Generator
- Multi-language support (Python, JavaScript, Java, Go, Rust)
- Intelligent code generation from descriptions
- Syntax validation & security checks
- Safe sandboxed execution
- Code quality metrics

### 🛡️ Enterprise-Ready
- Comprehensive error handling
- Security validation
- Detailed logging
- Full test coverage
- Production configuration

---

## 📊 System Architecture

```
                    NEURON (AI Powerhouse)
    ┌─────────────────────────────────────────────┐
    │  Chatbot │ Agent │ Code Generator │ Utilities│
    └────┬──────────┬──────────────┬──────────────┘
         │          │              │
    ┌────▼──────┐  ┌▼─────────┐   ┌▼────────────┐
    │   Memory  │  │   Tools  │   │  Validator  │
    │ Mgmt      │  │ Registry │   │  Executor   │
    └────┬──────┘  └▼─────────┘   └▼────────────┘
         │         │              │
         └─────────┴──────────────┘
                  │
         ┌────────▼────────┐
         │   LLM Manager   │
         │   (OpenAI)      │
         └─────────────────┘
```

---

## 🎯 Quick Start

### 1️⃣ Setup (2 minutes)
```bash
# Clone repository
git clone https://github.com/sakshum-cpu/ai-powerhouse.git
cd ai-powerhouse

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Test Everything (1 minute)
```bash
python setup_and_test.py
```

Expected output: ✅ All tests pass!

### 3️⃣ Run Examples (2 minutes)
```bash
# Try the chatbot
python examples/chatbot_example.py

# Try the agent
python examples/agent_example.py

# Try the code generator
python examples/code_gen_example.py
```

---

## 💻 Usage Examples

### Chatbot - Have Intelligent Conversations
```python
from chatbot.chatbot import Chatbot

# Create your AI assistant
bot = Chatbot(name="NEURON")

# Chat with it
response = bot.chat("What is machine learning?")
print(response)

# It remembers context!
response = bot.chat("Can you explain it more simply?")
print(response)
```

### Agent - Execute Complex Tasks
```python
from agent.agent import Agent

# Create autonomous agent
agent = Agent(name="TaskMaster")

# Execute tasks automatically
result = agent.execute_task(
    "Calculate 100 + 50, then find if it's prime, then generate 5 random numbers"
)
print(result["final_result"])
```

### Code Generator - Create Code Instantly
```python
from code_generator.generator import CodeGenerator

# Create code generator
gen = CodeGenerator()

# Generate code from description
result = gen.generate(
    "Create a function that checks if a number is palindrome",
    language="python"
)

print(result["code"])
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test module
pytest tests/test_chatbot.py -v

# Run with coverage
pytest tests/ --cov=chatbot --cov=agent --cov=code_generator
```

---

## 📁 Project Structure

```
NEURON (ai-powerhouse)
├── 🧠 chatbot/                 # Conversation engine
│   ├── chatbot.py             # Main chatbot class
│   └── memory.py              # Memory management
├── 🤖 agent/                   # Task execution engine
│   ├── agent.py               # Agent orchestrator
│   ├── tools.py               # Tool registry
│   ├── planner.py             # Task planner
│   └── executor.py            # Step executor
├── 💻 code_generator/          # Code generation
│   ├── generator.py           # Code generation
│   ├── validator.py           # Code validation
│   └── executor.py            # Safe execution
├── ⚙️ utils/                   # Utilities
│   ├── llm.py                 # LLM manager
│   ├── logger.py              # Logging
│   └── errors.py              # Exceptions
├── 📚 examples/                # Example scripts
│   ├── chatbot_example.py
│   ├── agent_example.py
│   └── code_gen_example.py
├── 🧪 tests/                   # Test suite
│   ├── test_chatbot.py
│   ├── test_agent.py
│   └── test_code_generator.py
├── 📖 docs/                    # Documentation
│   ├── API.md                 # API reference
│   └── ARCHITECTURE.md        # System design
├── 🚀 setup_and_test.py        # Setup script
├── ⚡ config.py                # Configuration
├── .env                        # Environment (configured ✅)
└── requirements.txt            # Dependencies
```

---

## ⚙️ Configuration

Edit `config.py` to customize NEURON:

```python
# LLM Settings
llm_model = "gpt-4"              # GPT model to use
llm_temperature = 0.7             # Creativity (0-1)
llm_max_tokens = 2000             # Response length

# Agent Settings
agent_max_iterations = 10         # Max task steps
agent_timeout = 300               # Timeout (seconds)

# Chatbot Settings
chatbot_memory_size = 10          # Messages to remember
chatbot_context_window = 5        # Context messages

# Code Generator
code_gen_timeout = 30             # Execution timeout
code_gen_sandbox = True           # Run in sandbox
```

---

## 🔑 API Reference

### Chatbot
```python
bot = Chatbot(name="NEURON")
bot.chat(user_input)              # Get response
bot.get_history()                 # Get all messages
bot.clear_history()               # Clear memory
bot.get_stats()                   # Get statistics
```

### Agent
```python
agent = Agent(name="TaskMaster")
agent.execute_task(task)          # Execute task
agent.add_tool(name, desc, func)  # Add custom tool
agent.get_history()               # Get execution history
```

### Code Generator
```python
gen = CodeGenerator()
gen.generate(description, language)   # Generate code
gen.generate_explanation(code)        # Explain code
gen.get_history()                     # Get history

validator = CodeValidator()
validator.validate_python(code)       # Check syntax
validator.check_security(code)        # Security check
```

---

## 🛡️ Security

✅ **Your API key is protected:**
- `.env` file is in `.gitignore` (never committed)
- Sensitive data is excluded from version control
- Code validation prevents dangerous operations
- Sandboxed code execution with timeout

**Never commit `.env` file to GitHub!**

---

## 📊 Performance

- **Chatbot**: Instant responses with context management
- **Agent**: Multi-step task execution in seconds
- **Code Generator**: Generate and validate code in <5 seconds

---

## 🚀 What's Next?

- ✅ Chatbot, Agent, Code Generator
- 🔜 Web UI Dashboard
- 🔜 Multi-model Support
- 🔜 Advanced Memory Management
- 🔜 Docker Deployment
- 🔜 Cloud Integration

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📖 Documentation

- [Quick Start Guide](QUICKSTART.md)
- [API Reference](docs/API.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 👨‍💻 Author

**Sakshum** - AI Enthusiast & Developer

---

## ⭐ Show Your Support

If you find NEURON useful, please:
- ⭐ Star the repository
- 🔗 Share it with friends
- 🐛 Report issues
- 💡 Suggest features

---

## 🎉 Ready to Use NEURON?

```bash
# Clone the repo
git clone https://github.com/sakshum-cpu/ai-powerhouse.git

# Setup
cd ai-powerhouse
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test it
python setup_and_test.py

# Start coding
python examples/chatbot_example.py
```

**Welcome to the future of AI! 🚀**

---

**NEURON** - *Where Intelligence Meets Code* 🧠⚡
