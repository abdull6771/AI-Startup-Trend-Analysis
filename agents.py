from typing import TypedDict
from config import llm, search_tool, news_prompt, summary_prompt, trend_prompt

# Define the state structure
class AnalysisState(TypedDict):
    topic: str
    articles: str
    summaries: str
    analysis: str

# Define agent nodes
def news_collector(state: AnalysisState) -> AnalysisState:
    chain = news_prompt | llm
    response = chain.invoke({"topic": state["topic"]})
    state["articles"] = response.content
    return state

def summary_writer(state: AnalysisState) -> AnalysisState:
    chain = summary_prompt | llm
    response = chain.invoke({"article": state["articles"]})
    state["summaries"] = response.content
    return state

def trend_analyzer(state: AnalysisState) -> AnalysisState:
    chain = trend_prompt | llm
    response = chain.invoke({"summary": state["summaries"]})
    state["analysis"] = response.content
    return state