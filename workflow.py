from langgraph.graph import StateGraph, END
from agents import AnalysisState, news_collector, summary_writer, trend_analyzer

# Build the workflow graph
def build_workflow():
    workflow = StateGraph(AnalysisState)

    # Add nodes
    workflow.add_node("news_collector", news_collector)
    workflow.add_node("summary_writer", summary_writer)
    workflow.add_node("trend_analyzer", trend_analyzer)

    # Define edges (flow)
    workflow.add_edge("news_collector", "summary_writer")
    workflow.add_edge("summary_writer", "trend_analyzer")
    workflow.add_edge("trend_analyzer", END)

    # Set entry point
    workflow.set_entry_point("news_collector")

    # Compile the graph
    return workflow.compile()