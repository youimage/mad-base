
import pytest
import asyncio
from agents.simple_agent import SimpleAgent
from llm_interface import LLMInterface

@pytest.mark.asyncio
async def test_agent_think():
    llm = LLMInterface()
    agent = SimpleAgent("TestAgent", "Test Role", llm)
    await agent.receive_message("Hello")
    response = await agent.think()
    assert isinstance(response, str)
    assert "[DummyLLM]" in response

@pytest.mark.asyncio
async def test_memory_limit():
    llm = LLMInterface()
    agent = SimpleAgent("MemoryTester", "Memory Role", llm)
    for i in range(5):
        await agent.receive_message(f"Message {i}")
    assert len(agent.memory) == agent.MAX_MEMORY
    assert agent.memory == ["Message 2", "Message 3", "Message 4"]
