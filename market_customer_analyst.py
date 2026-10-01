from crewai import Agent


def create_market_customer_analyst(llm):

    return Agent(
        role="Market and Customer Strategy Analyst",

        goal=(
            "Analyze the target market, customer segments, customer "
            "needs, pain points, buying behavior, market opportunities "
            "and potential growth segments."
        ),

        backstory=(
            "You are a market strategy consultant with expertise in "
            "customer segmentation, market positioning and consumer "
            "behavior. You convert business information into practical "
            "customer and market insights."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )
