# API Reference

## Chatbot

### `Chatbot` Class

```python
from chatbot.chatbot import Chatbot

chat = Chatbot(name="Assistant", system_prompt="You are helpful")
```

#### Methods

- `chat(user_input: str) -> str` - Process user input and get response
- `set_system_prompt(prompt: str) -> None` - Update system prompt
- `clear_history() -> None` - Clear conversation history
- `get_history() -> list` - Get conversation messages
- `get_stats() -> dict` - Get conversation statistics

## Agent

### `Agent` Class

```python
from agent.agent import Agent

agent = Agent(name="TaskBot")
```

#### Methods

- `execute_task(task: str) -> dict` - Execute a task
- `add_tool(name: str, description: str, func: callable) -> None` - Add custom tool
- `get_history() -> list` - Get execution history

### `ToolRegistry` Class

```python
from agent.tools import ToolRegistry

tools = ToolRegistry()
```

#### Methods

- `register(name: str, description: str, func: callable, args_schema: dict) -> None` - Register tool
- `execute(tool_name: str, **kwargs) -> Any` - Execute tool
- `get_tools() -> list` - Get all available tools

## Code Generator

### `CodeGenerator` Class

```python
from code_generator.generator import CodeGenerator

gen = CodeGenerator()
```

#### Methods

- `generate(description: str, language: str = "python", requirements: str = None) -> dict` - Generate code
- `generate_explanation(code: str, language: str = "python") -> str` - Explain code
- `get_history() -> list` - Get generation history

### `CodeExecutor` Class

```python
from code_generator.executor import CodeExecutor

executor = CodeExecutor()
```

#### Methods

- `execute(code: str, language: str = "python") -> dict` - Execute code safely

### `CodeValidator` Class

```python
from code_generator.validator import CodeValidator

validator = CodeValidator()
```

#### Methods

- `validate_python(code: str) -> Tuple[bool, List]` - Validate Python syntax
- `check_security(code: str) -> Tuple[bool, List]` - Check for security issues
- `check_quality(code: str) -> dict` - Check code quality

## Utilities

### `LLMManager` Class

```python
from utils.llm import get_llm_manager

llm = get_llm_manager()
response = llm.generate("Your prompt here")
```

#### Methods

- `generate(prompt: str, system_prompt: str = None) -> str` - Generate text
- `chat(messages: list) -> str` - Chat with message history
- `set_model(model: str) -> None` - Switch model

## Exceptions

- `AIError` - Base exception
- `LLMError` - LLM interaction errors
- `AgentError` - Agent execution errors
- `CodeExecutionError` - Code execution errors
- `ChatbotError` - Chatbot operation errors
- `ToolError` - Tool execution errors
