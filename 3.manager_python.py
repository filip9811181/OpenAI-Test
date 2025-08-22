from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish Translator",
    instructions="Translate text into Spanish."
)

french_agent = Agent(
    name="French Translator",
    instructions="Translate text into French."
)

italian_agent = Agent(
    name="Italian Translator",
    instructions="Translate text into Italian."
)

manager_agent = Agent(
    name="manager_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian",
        ),
    ],
)

async def main():
    msg = input("Translate 'hello' to Spanish, French and Italian for me!")

    orchestrator_output = await Runner.run(
        manager_agent, msg
    )
    
    print(f"Final Output: {orchestrator_output.final_output}")
    # for message in orchestrator_output.new_messages:
    #     print(f" - Translation step: {message.content}")
        
if __name__ == "__main__":
    asyncio.run(main())