import streamlit as st

from crew import run_business_consulting


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Business Consulting AI",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .agent-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📊 Business Consulting AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered multi-agent business strategy consulting team'
    '</div>',
    unsafe_allow_html=True
)


st.info(
    "Seven specialized AI consultants analyze your business and "
    "produce a structured strategic report."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🤖 Consulting Team")

    st.markdown(
        """
        **7 AI Specialists**

        🔎 Business Researcher

        👥 Market & Customer Analyst

        🏢 Competitor Analyst

        💰 Financial Analyst

        📈 Strategy Consultant

        ⚠️ Risk & Implementation Analyst

        👔 Senior Strategy Partner
        """
    )

    st.divider()

    st.caption(
        "Powered by CrewAI + Groq + GPT-OSS 120B"
    )


# --------------------------------------------------
# BUSINESS INFORMATION
# --------------------------------------------------

st.header("🏢 Tell Us About Your Business")


business_name = st.text_input(
    "Business Name",
    placeholder="Example: ABC Foods"
)


industry = st.text_input(
    "Industry",
    placeholder="Example: Food manufacturing"
)


country = st.text_input(
    "Country / Target Market",
    placeholder="Example: Pakistan"
)


business_stage = st.selectbox(
    "Business Stage",
    [
        "Idea / Startup",
        "Early-stage business",
        "Existing business",
        "Growing business",
        "Established company",
        "Other"
    ]
)


business_challenge = st.text_area(
    "What is the main business challenge?",
    placeholder=(
        "Example: Sales have stagnated during the last two years "
        "and we want to identify new growth opportunities."
    ),
    height=120
)


business_objective = st.text_area(
    "What is your main business objective?",
    placeholder=(
        "Example: Increase revenue, enter a new market, "
        "improve profitability, launch a new product, etc."
    ),
    height=120
)


target_customers = st.text_area(
    "Who are your target customers?",
    placeholder=(
        "Describe your main customers, customer segments, "
        "age groups, businesses, locations, etc."
    ),
    height=100
)


additional_information = st.text_area(
    "Additional Business Information",
    placeholder=(
        "Add any information that could help the consulting team "
        "understand your business."
    ),
    height=150
)


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

st.divider()


generate = st.button(
    "🚀 Generate Business Strategy",
    type="primary",
    use_container_width=True
)


# --------------------------------------------------
# RUN CONSULTING TEAM
# --------------------------------------------------

if generate:

    if not business_name.strip():
        st.error("Please enter the business name.")

    elif not industry.strip():
        st.error("Please enter the industry.")

    elif not business_challenge.strip():
        st.error("Please describe the main business challenge.")

    elif not business_objective.strip():
        st.error("Please describe the business objective.")

    else:

        st.divider()

        st.header("🤖 AI Consulting Team")

        progress = st.empty()

        progress.info(
            "The consulting team is analyzing your business. "
            "This may take several minutes because multiple AI "
            "specialists are working sequentially."
        )

        try:

            result = run_business_consulting(
                business_name=business_name,
                industry=industry,
                country=country,
                business_stage=business_stage,
                business_challenge=business_challenge,
                business_objective=business_objective,
                target_customers=target_customers,
                additional_information=additional_information
            )

            progress.success(
                "✅ Consulting analysis completed."
            )

            st.divider()

            st.header("📑 Business Strategy Report")

            report_text = str(result)

            st.markdown(report_text)

            st.divider()

            st.download_button(
                label="📥 Download Strategy Report",
                data=report_text,
                file_name=(
                    f"{business_name.replace(' ', '_')}"
                    "_business_strategy_report.md"
                ),
                mime="text/markdown",
                use_container_width=True
            )

        except Exception as e:

            progress.error(
                "The consulting team encountered an error."
            )

            st.error(
                f"Error details: {str(e)}"
            )

            st.info(
                "Check your GROQ_API_KEY in Streamlit Secrets "
                "and review the Streamlit deployment logs."
            )
