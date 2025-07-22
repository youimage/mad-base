
import asyncio
from agents.simple_agent import SimpleAgent
from communication import run_conversation
from llm_interface import LLMInterface
from config import CONFIG

async def main():
    llm = LLMInterface()
    agent1 = SimpleAgent(CONFIG["agent_1"]["name"], CONFIG["agent_1"]["role"], llm)
    agent2 = SimpleAgent(CONFIG["agent_2"]["name"], CONFIG["agent_2"]["role"], llm)
    await run_conversation(agent1, agent2, CONFIG["turns"])

if __name__ == "__main__":
    asyncio.run(main())
