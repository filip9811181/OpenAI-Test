from agents import Agent, WebSearchTool, function_tool, Runner

@function_tool
def save_results(output):
    db.insert({"output": output, "timestamp": datetime.time()})
    return "File saved successfully."

serach_agent = Agent(
    name="SearchAgent",
    instructions="Help the user search the internet and save results if asked",
    tools=[WebSearchTool(), save_results],
)

Runner.run_sync(serach_agent, input="What's the weather like in New York?")
