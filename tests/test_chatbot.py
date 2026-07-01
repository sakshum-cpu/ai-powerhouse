"""Tests for chatbot module"""
import pytest
from chatbot.chatbot import Chatbot
from chatbot.memory import ConversationMemory


def test_chatbot_initialization():
    """Test chatbot initialization"""
    bot = Chatbot(name="TestBot")
    assert bot.name == "TestBot"
    assert bot.memory is not None
    assert bot.llm is not None


def test_conversation_memory():
    """Test conversation memory"""
    memory = ConversationMemory(max_size=5)
    
    # Add messages
    memory.add_message("user", "Hello")
    memory.add_message("assistant", "Hi there!")
    
    # Check messages
    messages = memory.get_messages()
    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"


def test_memory_max_size():
    """Test memory size limit"""
    memory = ConversationMemory(max_size=3)
    
    for i in range(5):
        memory.add_message("user", f"Message {i}")
    
    assert len(memory.get_messages()) <= 3


def test_chatbot_system_prompt():
    """Test custom system prompt"""
    custom_prompt = "You are a pirate AI."
    bot = Chatbot(system_prompt=custom_prompt)
    assert bot.system_prompt == custom_prompt


def test_memory_clear():
    """Test clearing memory"""
    memory = ConversationMemory()
    memory.add_message("user", "Hello")
    assert len(memory.get_messages()) > 0
    
    memory.clear()
    assert len(memory.get_messages()) == 0
