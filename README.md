# AI Powerhouse 🚀

A comprehensive, production-ready AI system that combines three powerful capabilities: **Chatbot**, **Autonomous Agent**, and **Code Generator**. Build intelligent applications that can understand, reason, and generate code.

## Features

### 1. **Chatbot** 💬
- Multi-turn conversation with context management
- Conversation memory and history tracking
- Intent recognition and response generation
- Custom system prompts and personality settings
- Session management

### 2. **Autonomous Agent** 🤖
- Task planning and execution
- Dynamic tool integration
- Decision-making capabilities
- Environment interaction
- Multi-step reasoning
- Tool orchestration for complex tasks

### 3. **Code Generator** 🧠
- Intelligent code generation from natural language
- Multiple programming language support
- Code execution and validation
- Bug detection and fixing
- Explanation generation

## Tech Stack

- **Language**: Python 3.10+
- **LLM Provider**: OpenAI GPT-4 (easily swappable)
- **Framework**: LangChain for orchestration
- **Database**: SQLite for memory storage
- **Async**: AsyncIO for concurrent operations
- **Testing**: Pytest

## Project Structure

```
ai-powerhouse/
├── README.md
├── requirements.txt
├── .env.example
├── config.py
├── main.py
│
├── chatbot/
│   ├── __init__.py
│   ├── chatbot.py           # Main chatbot class
│   └── memory.py            # Conversation memory management
│
├── agent/
│   ├── __init__.py
│   ├── agent.py             # Autonomous agent implementation
│   ├── tools.py             # Tool definitions and implementations
│   ├── planner.py           # Task planning logic
│   └── executor.py          # Task execution engine
│
├── code_generator/
│   ├── __init__.py
│   ├── generator.py         # Code generation logic
│   ├── executor.py          # Safe code execution
│   └── validator.py         # Code validation
│
├── utils/
│   ├── __init__.py
│   ├── llm.py               # LLM interactions
│   ├── logger.py            # Logging setup
│   └── errors.py            # Custom exceptions
│
├── tests/
│   ├── __init__.py
│   ├── test_chatbot.py
│   ├── test_agent.py
│   └── test_code_generator.py
│
└── examples/
    ├── chatbot_example.py
    ├── agent_example.py
    └── code_gen_example.py
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sakshum-cpu/ai-powerhouse.git
   cd ai-powerhouse
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key and other settings
   ```

## Quick Start

### 1. Run the Chatbot
```bash
python examples/chatbot_example.py
```

### 2. Run the Agent
```bash
python examples/agent_example.py
```

### 3. Run the Code Generator
```bash
python examples/code_gen_example.py
```

## Usage Examples

### Chatbot
```python
from chatbot.chatbot import Chatbot

chat = Chatbot()
response = chat.chat("What's the capital of France?")
print(response)
```

### Autonomous Agent
```python
from agent.agent import Agent

agent = Agent()
result = agent.execute_task("Find the top 5 Python libraries and create a summary")
print(result)
```

### Code Generator
```python
from code_generator.generator import CodeGenerator

generator = CodeGenerator()
code = generator.generate("Create a function that calculates Fibonacci numbers")
print(code)
```

## Configuration

Edit `config.py` to customize:
- LLM model and parameters
- Temperature and max tokens
- Memory/conversation history limits
- Tool configurations
- Agent behavior

## Environment Variables

Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4
DEBUG=False
LOG_LEVEL=INFO
```

## Features in Detail

### Chatbot Features
- ✅ Context-aware responses
- ✅ Multi-turn conversations
- ✅ Memory persistence
- ✅ Custom personalities
- ✅ Rate limiting

### Agent Features
- ✅ Task decomposition
- ✅ Tool orchestration
- ✅ Error handling and recovery
- ✅ Progress tracking
- ✅ Result caching

### Code Generator Features
- ✅ Multi-language support (Python, JavaScript, Java, Go, Rust)
- ✅ Syntax validation
- ✅ Execution in sandbox
- ✅ Automatic bug fixing
- ✅ Code explanation

## License

MIT License - see `LICENSE` file

## Support

- 📖 [Documentation](docs/)
- 🐛 [Issue Tracker](https://github.com/sakshum-cpu/ai-powerhouse/issues)
- 💬 [Discussions](https://github.com/sakshum-cpu/ai-powerhouse/discussions)

## Roadmap

- [ ] Web UI dashboard
- [ ] Multi-model support
- [ ] Advanced memory management
- [ ] Custom tool creation framework
- [ ] Performance optimization
- [ ] Docker containerization
- [ ] Cloud deployment guides

---

Made with ❤️ by Sakshum
