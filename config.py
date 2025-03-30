import os
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Environment setup
os.environ["GROQ_API_KEY"] = "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"

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define tools
search_tool = DuckDuckGoSearchRun(max_results=5)

# Prompt templates
news_prompt = ChatPromptTemplate.from_template("""Collect recent news on Topic: {topic}""")
summary_prompt = ChatPromptTemplate.from_template("""Summarize the following articles: {article}""")
trend_prompt = ChatPromptTemplate.from_template(
    """Analyze trends from the following summaries and provide a detailed report identifying emerging trends and potential startup opportunities: Summary: {summary}"""
)