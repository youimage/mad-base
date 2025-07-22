
async def run_conversation(agent1, agent2, turns=3):
    await agent1.receive_message("Nice to meet you")
    for _ in range(turns):
        res1 = await agent1.think()
        print(f"{agent1.name}: {res1}")
        await agent1.send_message(res1, agent2)

        res2 = await agent2.think()
        print(f"{agent2.name}: {res2}")
        await agent2.send_message(res2, agent1)

def run_sync_conversation(agent1, agent2, turns=3):
    agent1.receive_message_sync("Nice to meet you")
    for _ in range(turns):
        loop = asyncio.get_event_loop()
        res1 = loop.run_until_complete(agent1.think())
        print(f"{agent1.name}: {res1}")
        agent1.send_message_sync(res1, agent2)

        res2 = loop.run_until_complete(agent2.think())
        print(f"{agent2.name}: {res2}")
        agent2.send_message_sync(res2, agent1)
