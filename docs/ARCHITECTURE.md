# Architecture

## System Overview

AI Powerhouse consists of three main components that work together:

```
┌─────────────────────────────────────────────────────────┐
│                   AI Powerhouse                         │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Chatbot    │  │    Agent     │  │Code Generator│  │
│  │              │  │              │  │              │  │
│  │- Memory      │  │- Task Plan   │  │- Generation  │  │
│  │- Conversation│  │- Tool Exec   │  │- Validation  │  │
│  │- Context Mgmt│  │- Reasoning   │  │- Execution   │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
└─────────┼──────────────────┼──────────────────┼─────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
    │   LLM   │        │ Tools   │        │ Memory  │
    │ Manager │        │Registry │        │ Storage │
    └─────────┘        └─────────┘        └─────────┘
```

## Component Architecture

### 1. Chatbot Module

**Purpose**: Conversational AI with context management

**Key Components**:
- `Chatbot` - Main interface for conversations
- `ConversationMemory` - Manages message history

**Data Flow**:
1. User input received
2. Message added to memory
3. LLM processes with context
4. Response added to memory
5. Response returned to user

### 2. Agent Module

**Purpose**: Autonomous task execution with reasoning

**Key Components**:
- `Agent` - Main task executor
- `TaskPlanner` - Breaks tasks into steps
- `ToolRegistry` - Manages available tools

**Data Flow**:
1. Task received
2. Planner creates execution plan
3. Steps executed sequentially
4. Tool registry invoked for tool actions
5. Results synthesized
6. Final output returned

### 3. Code Generator Module

**Purpose**: Intelligent code generation and validation

**Key Components**:
- `CodeGenerator` - Generates code from descriptions
- `CodeValidator` - Validates syntax and security
- `CodeExecutor` - Safely executes generated code

**Data Flow**:
1. Code description received
2. LLM generates code
3. Validator checks syntax and security
4. Code can be executed in sandbox
5. Results and metrics returned

## Data Flow

### User Request Flow

```
User Input
    │
    ├─► [Chatbot] ─► Memory ─► LLM ─► Response
    │
    ├─► [Agent] ─► Planner ─► Tools ─► LLM ─► Result
    │
    └─► [Generator] ─► Validator ─► Executor ─► Output
```

## Configuration

All components use centralized configuration via `config.py`:

- LLM Settings (model, temperature, tokens)
- Application Settings (debug, logging)
- Component Settings (timeouts, limits)

## Error Handling

**Hierarchy**:
```
AIError (base)
├── LLMError
├── AgentError
│   └── ToolError
├── CodeExecutionError
└── ChatbotError
```

Each component catches and re-raises as appropriate type.

## Extensibility

### Adding Custom Tools

```python
agent = Agent()
agent.add_tool(
    name="my_tool",
    description="What it does",
    func=my_function
)
```

### Custom LLM Provider

Replace `LLMManager` in `utils/llm.py` with your provider.

### Custom System Prompts

```python
chatbot = Chatbot(system_prompt="Your custom prompt")
```

## Performance Considerations

1. **Memory Management**: Messages are pruned based on `CHATBOT_MEMORY_SIZE`
2. **Token Limits**: Configured in `config.py`
3. **Timeouts**: Agent and code execution have configurable timeouts
4. **Caching**: Consider implementing for repeated queries

## Security

1. **Code Validation**: All generated code is validated
2. **Sandbox Execution**: Code runs with timeout protection
3. **Security Checks**: Dangerous patterns detected
4. **Input Validation**: All inputs validated before processing
