from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    Guardrail,
    GuardrailTripwireTriggered,
)

from pydantic import BaseModel


class ChurnDetectionOutput(BaseModel):
    is_churn_risk: bool
    reasoning: str


churn_detection_agent = Agent(
    name="Churn Detection Agent",
    instructions="Identify if the user message indicates a potential customer churn risk.",
    output_type=ChurnDetectionOutput,
)


@input_guardrail
async def churn_detection_tripwire(
    ctx: RunContextWrapper[None], agent: Agent, input: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(churn_detection_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_churn_risk,
    )


customer_support_agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[
        Guardrail(guardrail_function=churn_detection_tripwire),
    ],
)


async def main():
    # This should be ok
    await Runner.run(customer_support_agent, "Hello!")
    print("Hello ran successfully")
# This should trip the guardrail
    try:
        await Runner.run(agent, "I think I might cancel my subscription")
        print("Guardrail didn't trip – this is unexpected")
    except GuardrailTripwireTriggered:
        print("Churn detection guardrail tripped")

if __name__ == "__main__":
    asyncio.run(main())
