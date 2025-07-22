
import os
import asyncio

USE_OPENAI = os.getenv("USE_OPENAI", "0") == "1"

if USE_OPENAI:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class LLMInterface:
    async def generate_response(self, prompt: str) -> str:
        if USE_OPENAI:
            try:
                response = await asyncio.to_thread(
                    client.chat.completions.create,
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=100,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                return f"[OpenAI Error] {e}"
        else:
            # Dummy lightweight LLM response (for local LLM substitution)
            await asyncio.sleep(0.05)
            # Simple mimic that reverses the prompt
            return f"[DummyLLM] {prompt[::-1]}"
