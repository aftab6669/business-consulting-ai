from crewai import Crew, Task, Process

from llm import get_llm

from business_researcher import create_business_researcher
from market_customer_analyst import create_market_customer_analyst
from competitor_analyst import create_competitor_analyst
from financial_analyst import create_financial_analyst
from strategy_consultant import create_strategy_consultant
from risk_implementation_analyst import create_risk_implementation_analyst
from senior_strategy_partner import create_senior_strategy_partner


def run_business_consulting(
    business_name,
    industry,
    country,
    business_stage,
    business_challenge,
    business_objective,
    target_customers,
    additional_information
):

    llm = get_llm()

    # --------------------------------------------------
    # CREATE AGENTS
    # --------------------------------------------------

    researcher = create_business_researcher(llm)

    customer_analyst = create_market_customer_analyst(llm)

    competitor_analyst = create_competitor_analyst(llm)

    financial_analyst = create_financial_analyst(llm)

    strategy_consultant = create_strategy_consultant(llm)

    risk_analyst = create_risk_implementation_analyst(llm)

    senior_partner = create_senior_strategy_partner(llm)

    # --------------------------------------------------
    # COMMON BUSINESS BRIEF
    # --------------------------------------------------

    business_brief = f"""
BUSINESS CONSULTING CLIENT BRIEF

Business Name:
{business_name}

Industry:
{industry}

Country / Market:
{country}

Business Stage:
{business_stage}

Business Challenge:
{business_challenge}

Business Objective:
{business_objective}

Target Customers:
{target_customers}

Additional Information:
{additional_information}
"""

    # --------------------------------------------------
    # TASK 1 — BUSINESS RESEARCH
    # --------------------------------------------------

    research_task = Task(
        description=f"""
{business_brief}

Conduct a structured business and industry analysis.

Analyze:

1. Business situation
2. Industry environment
3. Important industry trends
4. External opportunities
5. External threats
6. Key business issues
7. Strategic implications

Do not invent facts.

If information is unavailable, explicitly state:
"Information not provided."

Produce a structured consulting analysis.
""",

        expected_output="""
A structured business and industry research report containing:

- Business situation
- Industry analysis
- Key trends
- Opportunities
- Threats
- Strategic implications
- Information gaps
""",

        agent=researcher
    )

    # --------------------------------------------------
    # TASK 2 — MARKET & CUSTOMER
    # --------------------------------------------------

    customer_task = Task(
        description=f"""
{business_brief}

Analyze the market and customers.

Examine:

1. Target customer
2. Potential customer segments
3. Customer needs
4. Customer pain points
5. Buying considerations
6. Potential market opportunities
7. Possible growth segments
8. Customer-related risks

Clearly distinguish assumptions from information supplied by the client.
""",

        expected_output="""
A structured market and customer analysis covering:

- Customer segments
- Customer needs
- Pain points
- Market opportunities
- Growth segments
- Customer risks
- Strategic implications
""",

        agent=customer_analyst
    )

    # --------------------------------------------------
    # TASK 3 — COMPETITOR
    # --------------------------------------------------

    competitor_task = Task(
        description=f"""
{business_brief}

Conduct a competitive strategy analysis.

Analyze:

1. Likely competitor categories
2. Competitive positioning
3. Products/services
4. Pricing considerations
5. Distribution considerations
6. Competitive advantages
7. Competitive weaknesses
8. Market gaps
9. Differentiation opportunities

Do not invent specific competitor facts when the client has not
provided sufficient information.

Clearly identify assumptions and information gaps.
""",

        expected_output="""
A competitive intelligence report containing:

- Competitor landscape
- Positioning
- Competitive factors
- Market gaps
- Differentiation opportunities
- Competitive threats
- Information limitations
""",

        agent=competitor_analyst
    )

    # --------------------------------------------------
    # TASK 4 — FINANCIAL
    # --------------------------------------------------

    financial_task = Task(
        description=f"""
{business_brief}

Conduct a business and financial analysis.

Analyze:

1. Business model
2. Revenue sources
3. Cost structure
4. Pricing considerations
5. Profitability drivers
6. Potential financial opportunities
7. Investment requirements
8. Financial risks
9. Missing financial information

Do NOT invent financial numbers.

Where numbers are unavailable, explain which numbers management
should collect.

Include useful financial KPIs where appropriate.
""",

        expected_output="""
A business and financial analysis covering:

- Business model
- Revenue drivers
- Cost drivers
- Pricing
- Profitability considerations
- Investment requirements
- Financial risks
- Recommended KPIs
- Missing financial data
""",

        agent=financial_analyst
    )

    # --------------------------------------------------
    # TASK 5 — STRATEGY
    # --------------------------------------------------

    strategy_task = Task(
        description="""
Using the outputs of the previous consulting tasks, develop a
strategic analysis for the client.

Develop several realistic strategic options.

For every strategic option explain:

1. Strategic idea
2. Rationale
3. Expected benefits
4. Required capabilities
5. Resources required
6. Main risks
7. Implementation requirements
8. Key assumptions

Do not use unsupported financial projections.

Finish with a clear strategic direction based on the evidence
available in the previous analyses.
""",

        expected_output="""
A strategic analysis containing:

- Strategic priorities
- Multiple strategic options
- Benefits
- Required capabilities
- Risks
- Assumptions
- Strategic direction
""",

        agent=strategy_consultant,

        context=[
            research_task,
            customer_task,
            competitor_task,
            financial_task
        ]
    )

    # --------------------------------------------------
    # TASK 6 — RISK & IMPLEMENTATION
    # --------------------------------------------------

    risk_task = Task(
        description="""
Using all previous analyses, develop a practical implementation
and risk management plan.

Identify:

1. Strategic risks
2. Financial risks
3. Operational risks
4. Market risks
5. Competitive risks
6. Execution risks

Then develop:

- 0–90 day action plan
- 3–6 month priorities
- 6–12 month priorities
- Longer-term roadmap
- Recommended KPIs
- Management milestones

Make the roadmap practical and measurable.
""",

        expected_output="""
A practical implementation plan containing:

- Risk register
- 90-day plan
- 3–6 month plan
- 6–12 month plan
- Long-term roadmap
- KPIs
- Management milestones
""",

        agent=risk_analyst,

        context=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
            strategy_task
        ]
    )

    # --------------------------------------------------
    # TASK 7 — FINAL REPORT
    # --------------------------------------------------

    final_report_task = Task(
        description=f"""
You are the Senior Strategy Partner.

Prepare the final professional consulting report for:

{business_name}

{business_brief}

You have received the work of the specialist consultants.

Integrate their findings into ONE coherent business strategy report.

The report must contain:

1. Executive Summary

2. Business Situation

3. Industry Analysis

4. Market and Customer Analysis

5. Competitive Analysis

6. Business Model Analysis

7. Financial Considerations

8. SWOT Analysis

9. Strategic Issues

10. Strategic Options

11. Strategic Direction

12. Growth Strategy

13. Risk Analysis

14. Implementation Roadmap

15. 90-Day Action Plan

16. 12-Month Action Plan

17. Key Performance Indicators

18. Key Assumptions

19. Information Gaps

20. Conclusion

IMPORTANT:

- Do not invent facts.
- Do not invent financial figures.
- Clearly identify assumptions.
- Clearly identify missing information.
- Distinguish client-provided information from analysis.
- Keep recommendations practical.
- Use professional consulting language.
- Avoid unnecessary repetition.
""",

        expected_output="""
A complete professional business strategy consulting report in
well-structured Markdown with headings, tables where useful,
strategic analysis, risks, implementation roadmap and KPIs.
""",

        agent=senior_partner,

        context=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
            strategy_task,
            risk_task
        ]
    )

    # --------------------------------------------------
    # BUILD CREW
    # --------------------------------------------------

    crew = Crew(
        agents=[
            researcher,
            customer_analyst,
            competitor_analyst,
            financial_analyst,
            strategy_consultant,
            risk_analyst,
            senior_partner
        ],

        tasks=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
            strategy_task,
            risk_task,
            final_report_task
        ],

        process=Process.sequential,

        verbose=True
    )

    # --------------------------------------------------
    # RUN CREW
    # --------------------------------------------------

    result = crew.kickoff()

    return result
