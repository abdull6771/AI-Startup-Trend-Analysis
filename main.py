from workflow import build_workflow
from agents import AnalysisState

def run_analysis(topic: str):
    app = build_workflow()
    initial_state = {"topic": topic, "articles": "", "summaries": "", "analysis": ""}
    try:
        result = app.invoke(initial_state)
        print("\nArticles:")
        print(result["articles"])
        print("\nSummaries:")
        print(result["summaries"])
        print("\nTrend Analysis and Potential Startup Opportunities:")
        print(result["analysis"])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    topic = "Artificial Intelligence in Healthcare"  # Hardcoded for simplicity; could use input()
    run_analysis(topic)