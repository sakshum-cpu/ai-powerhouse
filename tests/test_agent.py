"""Tests for agent module"""
import pytest
from agent.agent import Agent
from agent.tools import ToolRegistry


def test_agent_initialization():
    """Test agent initialization"""
    agent = Agent(name="TestAgent")
    assert agent.name == "TestAgent"
    assert agent.tools is not None
    assert agent.planner is not None


def test_tool_registry():
    """Test tool registry"""
    registry = ToolRegistry()
    
    # Check default tools are registered
    tools = registry.get_tools()
    tool_names = [t["name"] for t in tools]
    
    assert "calculator" in tool_names
    assert "web_search" in tool_names


def test_custom_tool_registration():
    """Test registering custom tool"""
    agent = Agent()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    agent.add_tool("doubler", "Doubles a number", dummy_tool)
    
    tools = agent.tools.get_tools()
    tool_names = [t["name"] for t in tools]
    assert "doubler" in tool_names


def test_calculator_tool():
    """Test calculator tool"""
    registry = ToolRegistry()
    result = registry.execute("calculator", expression="2 + 2")
    assert "4" in result


def test_agent_execution_history():
    """Test agent tracks execution history"""
    agent = Agent()
    assert len(agent.get_history()) == 0
