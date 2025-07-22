
import asyncio

class BaseAgent:
    MAX_MEMORY = 3  # Number of recent messages to retain in memory

    def __init__(self, name, role, llm):
        self.name = name
        self.role = role
        self.llm = llm
        self.memory = []

    def receive_message_sync(self, msg):
        if len(self.memory) >= self.MAX_MEMORY:
            self.memory.pop(0)
        self.memory.append(msg)

    async def receive_message(self, msg):
        self.receive_message_sync(msg)

    async def think(self):
        prompt = "\n".join(self.memory[-self.MAX_MEMORY:])
        response = await self.llm.generate_response(prompt)
        self.receive_message_sync(response)
        return response

    def send_message_sync(self, msg, recipient):
        recipient.receive_message_sync(msg)

    async def send_message(self, msg, recipient):
        self.send_message_sync(msg, recipient)
