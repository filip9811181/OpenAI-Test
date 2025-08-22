from agents import Agent, WebSearchTool, function_tool, Runner


@function_tool
def get_weather(city: str) -> str:
    print(f"The weather in {city} is sunny")
    return f"The weather in {city} is sunny"
    
    
weather_agent = Agent(
    name="Weather agent",
    instructions="You are a helpful agent who can talk to users about the weather.",
    tools=[get_weather],
)

Runner.run_sync(weather_agent, input="What's the weather like in New York?")