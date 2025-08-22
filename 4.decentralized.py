from agents import Agent, Runner, function_tool
import asyncio

@function_tool
def search_knowledge_base(output : str) -> str:
    print(f"search_knowledge_base -------------------------")
    return f"save_results: {output}" 
    
@function_tool
def initiate_purchase_order(output : str) -> str:
    print(f"initiate_purchase_order -------------------------")
    return f"save_results: {output}" 
    
@function_tool
def track_order_status(output : str) -> str:
    print(f"track_order_status -------------------------")
    return f"save_results: {output}" 
    
@function_tool
def initiate_refund_process(output : str) -> str:
    print(f"initiate_refund_process -------------------------")
    return f"save_results: {output}" 

technical_support_agent = Agent(
    name="Technical Support Agent",
    instructions=(
        "You provide expert assistance with resolving technical issues, "
        "system outages, or product troubleshooting from the knowledge base"
    ),
    tools=[search_knowledge_base] # Replace with actual tool
)

sales_assistant_agent = Agent(
    name="Sales Assistant Agent",
    instructions=(
        "You help enterprise clients browse the product catalog, recommend "
        "suitable solutions, and facilitate purchase transactions."
    ),
    tools=[initiate_purchase_order] # Replace with actual tool
)

order_management_agent = Agent(
    name="Order Management Agent",
    instructions=(
        "You assist clients with inquiries regarding order tracking, "
        "delivery schedules, and processing returns or refunds."
    ),
    tools=[track_order_status, initiate_refund_process] # Replace with actual tools
)


triage_agent = Agent(
    name="Triage Agent",
    instructions="You act as the first point of contact, assessing customer "
                 "queries and directing them promptly to the correct specialized agent.",
    handoffs=[technical_support_agent, sales_assistant_agent, order_management_agent],
)


async def run_triage():
    output = await Runner.run(
        triage_agent,
        input("Could you please provide an update on the delivery timeline for our recent purchase?")
    )

    print(f"Output: {output.final_output}")

if __name__ == "__main__":
    asyncio.run(run_triage())