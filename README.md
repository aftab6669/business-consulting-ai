# 📊 Business Consulting AI

An AI-powered multi-agent business consulting application built with:

- CrewAI
- Groq
- GPT-OSS 120B
- Streamlit

## AI Consulting Team

The application uses seven specialized agents:

1. Business Researcher
2. Market & Customer Analyst
3. Competitor Analyst
4. Financial Analyst
5. Strategy Consultant
6. Risk & Implementation Analyst
7. Senior Strategy Partner

## Architecture

User
↓
Streamlit
↓
CrewAI
↓
Specialized AI Consultants
↓
Senior Strategy Partner
↓
Business Strategy Report

## Deployment

The application is designed for deployment through Streamlit Community Cloud.

No local Python installation is required for the deployment workflow.

## API Key

The application requires:

GROQ_API_KEY

Add the key through Streamlit Secrets.

Never commit API keys to GitHub.
