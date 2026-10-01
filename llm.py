import os
import streamlit as st
from crewai import LLM


def get_groq_api_key():
    """Get Groq API key from Streamlit Secrets or environment variables."""

    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY")


def get_llm():
    """Create the CrewAI LLM connected to Groq."""

    api_key = get_groq_api_key()

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add it to Streamlit Secrets."
        )

    return LLM(
        model="openai/gpt-oss-120b",
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key,
        temperature=0.2,
        max_tokens=8000,
    )
