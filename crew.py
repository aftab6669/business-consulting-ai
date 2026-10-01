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
    additional_information,
):

    # ==========================================================
    # 1. CREATE LLM
    # ==========================================================

    llm = get_llm()

    # ==========================================================
    # 2. CREATE CONSULTING AGENTS
    # ==========================================================

    researcher = create_business_researcher(llm)

    customer_analyst = create_market_customer_analyst(llm)

    competitor_analyst = create_competitor_analyst(llm)

    financial_analyst = create_financial_analyst(llm)

    strategy_consultant = create_strategy_consultant(llm)

    risk_analyst = create_risk_implementation_analyst(llm)

    senior_partner = create_senior_strategy_partner(llm)

    # ==========================================================
    # 3. BUSINESS BRIEF
    # ==========================================================

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

IMPORTANT CONSULTING RULES:
- Use only information provided by the client and reasonable analytical
  assumptions.
- Clearly label assumptions.
- Do not invent financial figures.
- Do not present assumptions as verified facts.
- Identify important information gaps.
"""

    # ==========================================================
    # 4. TASK 1 — BUSINESS RESEARCH
    # ==========================================================

    research_task = Task(
        description=f"""
{business_brief}

You are the Business Research Consultant.

Analyze the client's business and its broader industry environment.

Cover:

1. Current business situation
2. Industry environment
3. Important industry trends
4. External opportunities
5. External threats
6. Major business issues
7. Strategic implications
8. Information gaps

Do not invent specific market statistics or facts.

If information is unavailable, clearly state:
"Information not provided."

Produce a structured consulting analysis.
""",
        expected_output="""
A structured business and industry research report containing:

- Business situation
- Industry analysis
- Industry trends
- Opportunities
- Threats
- Strategic implications
- Information gaps
""",
        agent=researcher,
    )

    # ==========================================================
    # 5. TASK 2 — MARKET & CUSTOMER
    # ==========================================================

    customer_task = Task(
        description=f"""
{business_brief}

You are the Market and Customer Analyst.

Analyze the target market and customers.

Cover:

1. Target customer profile
2. Customer segments
3. Customer needs
4. Customer pain points
5. Buying considerations
6. Potential market opportunities
7. Growth segments
8. Customer-related risks
9. Strategic implications

Clearly distinguish client-provided information from analytical assumptions.
""",
        expected_output="""
A structured market and customer analysis containing:

- Customer profile
- Customer segments
- Customer needs
- Pain points
- Buying considerations
- Market opportunities
- Growth segments
- Customer risks
- Strategic implications
""",
        agent=customer_analyst,
    )

    # ==========================================================
    # 6. TASK 3 — COMPETITOR ANALYSIS
    # ==========================================================

    competitor_task = Task(
        description=f"""
{business_brief}

You are the Competitive Intelligence Consultant.

Analyze the competitive environment.

Cover:

1. Likely competitor categories
2. Competitive positioning
3. Products and services
4. Pricing considerations
5. Distribution considerations
6. Potential competitive advantages
7. Potential competitive weaknesses
8. Market gaps
9. Differentiation opportunities
10. Competitive threats

Do not invent specific competitor facts.

If specific competitor information is unavailable, discuss
competitor categories and explain what information should be collected.
""",
        expected_output="""
A competitive intelligence report containing:

- Competitor landscape
- Competitive positioning
- Competitive factors
- Market gaps
- Differentiation opportunities
- Competitive threats
- Information gaps
""",
        agent=competitor_analyst,
    )

    # ==========================================================
    # 7. TASK 4 — FINANCIAL ANALYSIS
    # ==========================================================

    financial_task = Task(
        description=f"""
{business_brief}

You are the Business and Financial Analyst.

Analyze the business model and financial drivers.

Cover:

1. Business model
2. Revenue sources
3. Cost structure
4. Pricing considerations
5. Profitability drivers
6. Investment requirements
7. Financial opportunities
8. Financial risks
9. Financial information gaps
10. Recommended financial KPIs

Do NOT invent financial numbers.

Where financial data is unavailable, identify the data management
should collect before making investment or expansion decisions.
""",
        expected_output="""
A business and financial analysis containing:

- Business model
- Revenue drivers
- Cost drivers
- Pricing considerations
- Profitability drivers
- Investment requirements
- Financial opportunities
- Financial risks
- Financial KPIs
- Missing financial information
""",
        agent=financial_analyst,
    )

    # ==========================================================
    # 8. TASK 5 — STRATEGY
    # ==========================================================

    strategy_task = Task(
        description="""
Review the outputs of the Business Research, Market and Customer,
Competitive Intelligence, and Financial Analysis consultants.

Develop practical strategic options.

For each strategic option explain:

1. Strategic idea
2. Strategic rationale
3. Expected benefits
4. Required capabilities
5. Required resources
6. Main risks
7. Implementation requirements
8. Key assumptions

Develop several realistic alternatives.

Do not invent unsupported financial projections.

Conclude by identifying the strategic priorities that deserve
management attention based on the available evidence.
""",
        expected_output="""
A strategic analysis containing:

- Strategic priorities
- Multiple strategic options
- Strategic rationale
- Expected benefits
- Required capabilities
- Required resources
- Risks
- Assumptions
- Strategic priorities
""",
        agent=strategy_consultant,
        context=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
        ],
    )

    # ==========================================================
    # 9. TASK 6 — RISK & IMPLEMENTATION
    # ==========================================================

    risk_task = Task(
        description="""
Review all previous consulting analyses.

Develop a practical risk management and implementation plan.

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
- Management milestones
- Recommended KPIs

Make the implementation plan practical and measurable.

Do not invent unsupported financial targets.
""",
        expected_output="""
A practical implementation and risk report containing:

- Risk register
- Risk mitigation actions
- 90-day action plan
- 3–6 month priorities
- 6–12 month priorities
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
            strategy_task,
        ],
    )

    # ==========================================================
    # 10. TASK 7 — FINAL SENIOR PARTNER REPORT
    # ==========================================================

    final_report_task = Task(
        description=f"""
You are the Senior Strategy Partner.

Prepare the final professional consulting report for:

Business:
{business_name}

{business_brief}

You have received reports from six specialist consultants.

Integrate their findings into ONE coherent business strategy report.

The final report must contain the following sections:

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

IMPORTANT QUALITY RULES:

- Do not invent facts.
- Do not invent financial figures.
- Clearly distinguish facts from assumptions.
- Clearly identify missing information.
- Do not blindly accept previous consultant assumptions.
- Resolve contradictions where possible.
- Highlight important uncertainties.
- Keep recommendations practical.
- Use professional management consulting language.
- Avoid unnecessary repetition.
- Use tables where they improve clarity.
""",
        expected_output="""
A complete professional business strategy consulting report
written in well-structured Markdown.

The report should contain:

- Executive summary
- Business analysis
- Industry analysis
- Market and customer analysis
- Competitive analysis
- Business model analysis
- Financial considerations
- SWOT analysis
- Strategic options
- Strategic direction
- Growth strategy
- Risk analysis
- Implementation roadmap
- 90-day action plan
- 12-month action plan
- KPIs
- Assumptions
- Information gaps
- Conclusion
""",
        agent=senior_partner,
        context=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
            strategy_task,
            risk_task,
        ],
    )

    # ==========================================================
    # 11. BUILD CREW
    # ==========================================================

    crew = Crew(
        agents=[
            researcher,
            customer_analyst,
            competitor_analyst,
            financial_analyst,
            strategy_consultant,
            risk_analyst,
            senior_partner,
        ],
        tasks=[
            research_task,
            customer_task,
            competitor_task,
            financial_task,
            strategy_task,
            risk_task,
            final_report_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    # ==========================================================
    # 12. RUN CONSULTING TEAM
    # ==========================================================

    result = crew.kickoff()

    return result
