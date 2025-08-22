from agents import Agent, WebSearchTool, function_tool, Runner

@function_tool
def save_results(output : str) -> str:
    print(f"-------------------------")
    print(output)
    print(f"-------------------------")
    return f"Results saved: {output}" 

serach_agent = Agent(
    name="SearchAgent",
    instructions="Help the user search the internet and save results if asked",
    tools=[WebSearchTool(), save_results],
)

result = Runner.run_sync(serach_agent, "What is disney company? save results")
print(result.final_output)
