import os 
from dotenv import load_dotenv
from agents import Agent, Runner ,OpenAIChatCompletionsModel,AsyncOpenAI,function_tool,set_tracing_disabled
from agents.run import RunConfig
set_tracing_disabled(disabled=True)
load_dotenv()

gemini_key=os.getenv("Gemini_key")

client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

config = RunConfig(
    model=model,
    model_provider=client,
)
@function_tool
async def add(a:int,b:int) ->int:
    """
    Add to Numbers

    Args:
    a :the first number.
    b :the second number.

    """
    return a + b + 1
agent = Agent(
    name="Assistant",
    instructions='You r Helpful agent',
    tools=[add],
)
result = Runner.run_sync(agent," What is Number 2 + 3", run_config=config)
print(result.final_output)