# AI Startup Trend Analysis Agent

This project implements a modular AI-powered agent that analyzes recent trends and startup opportunities in a specified topic, with a focus on "Artificial Intelligence in Healthcare" as the default example. Built using [LangGraph](https://github.com/langchain-ai/langgraph) and powered by the Grok LLaMA model via [Grok API](https://groq.com/), the agent collects news articles, summarizes them, and identifies emerging trends and potential startup ideas.

## Features
- **Modular Design**: Separates configuration, agent logic, workflow, and execution into distinct files.
- **Three-Stage Workflow**:
  1. **News Collector**: Gathers recent articles using DuckDuckGo search.
  2. **Summary Writer**: Summarizes collected articles.
  3. **Trend Analyzer**: Analyzes summaries to identify trends and startup opportunities.
- **Extensible**: Easily adaptable to other topics or LLMs.

## Project Structure
```
ai-healthcare-agent/
├── config.py       # Configuration, LLM, and tool setup
├── agents.py       # Agent functions and state definition
├── workflow.py     # LangGraph workflow construction
├── main.py         # Entry point and execution logic
└── README.md       # Project documentation
```

## Prerequisites
- Python 3.8+
- A Grok API key (available from [Grok](https://groq.com/))

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdull6771/AI-Startup-Trend-Analysis
   cd AI-Startup-Trend-Analysis
   ```

2. **Install Dependencies**:
   ```bash
   pip install langchain-groq langchain-community langgraph duckduckgo-search
   ```

3. **Set Up Environment**:
   - The API key is hardcoded in `config.py` for simplicity. For security, replace it with an environment variable:
     ```bash
     export GROQ_API_KEY="your-grok-api-key"
     ```
     Then update `config.py` to use `os.getenv("GROQ_API_KEY")`.

## Usage
1. **Run the Agent**:
   ```bash
   python main.py
   ```
   - By default, it analyzes "Artificial Intelligence in Healthcare".
   - Output includes articles, summaries, and a trend analysis report.

2. **Customize the Topic**:
   - Edit `main.py` to change the `topic` variable:
     ```python
     topic = "Your Custom Topic"
     run_analysis(topic)
     ```

## Example Output
```
Articles:
Here are some recent news articles on the topic of Artificial Intelligence in Healthcare:
1. AI-Powered Chatbots for Mental Health Support (February 2023)...

Summaries:
Here's a summary of the 10 news articles on the topic of Artificial Intelligence in Healthcare:
- Mental Health Support: AI-powered chatbots can provide effective mental health support...

Trend Analysis and Potential Startup Opportunities:
Emerging Trends in Artificial Intelligence (AI) in Healthcare:
1. Personalization: AI is being used to provide personalized care plans...
Potential Startup Opportunities:
1. AI-powered Mental Health Platforms: Develop AI-powered chatbots...
```

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (create one if needed).

## Acknowledgments
- Built with [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain).
- Powered by [Grok](https://groq.com/) LLaMA model.
- Inspired by advancements in AI-driven healthcare solutions.

## Contact
For questions or suggestions, open an issue or reach out to [abdulll8392@gmail.com](mailto:abdulll8392@gmail.com).
