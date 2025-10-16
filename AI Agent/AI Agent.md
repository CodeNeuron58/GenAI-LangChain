AI Agent — README

This folder contains an example Jupyter notebook `Agent.ipynb` that demonstrates building a small LangChain-style agent using a Cohere chat model, a community search tool (DuckDuckGo), and a simple weather tool. The notebook shows how to load secrets, initialize the LLM, pull a reAct prompt template from the LangChain hub, register tools, create an agent, and run queries through an executor.

Contents
- `Agent.ipynb` — the working notebook with step-by-step examples.

Prerequisites
- Python 3.8+ (a modern Python 3 runtime)
- Install required packages (the notebook assumes LangChain, langchain_cohere, langchain_community and requests). Example pip line:

```bash
pip install langchain langchain-cohere langchain-community requests python-dotenv
```

- A `.env` file with your Cohere API key, e.g.:

```
COHERE_API_KEY=your_cohere_api_key_here
```

Quick overview of the notebook steps

1) Load environment and validate API key

- The notebook loads environment variables with `python-dotenv` and checks `COHERE_API_KEY` is present.

2) Import model and tools

- Uses `ChatCohere` from `langchain_cohere` for the LLM.
- Demonstrates a community search tool: `DuckDuckGoSearchRun`.
- Shows a simple weather tool defined with the `@tool` decorator that can be wired into the agent.

3) Initialize the LLM

- The notebook initializes `ChatCohere` with `cohere_api_key` and a model name (example: `command-a-03-2025`).

4) Pull a prompt template from the LangChain hub

- It pulls the `hwchase17/react` template to use as the agent prompt (reAct style).

5) Create agent and executor

- The notebook creates a reAct agent via `create_react_agent(...)`, registers tools (`search_tool`, `get_weather_data`), and wraps the agent with `AgentExecutor`.

6) Run example queries

- Simple LLM query examples such as: "What is the capital of France".
- Agent examples: "What’s the current weather in New York?" — the agent decides whether to use the weather tool or a search tool and then returns a formatted result.

Notes & suggestions
- The provided `get_weather_data` tool in the notebook is a placeholder. Replace the `url = "api endpoint"` with a real weather API endpoint (for example OpenWeather) and add API key handling.
- Network calls require internet access and valid API keys. If you don't want to provide a live API key, keep the examples as demonstrations of wiring rather than runnable examples.
- Consider adding basic error handling around network calls to make the notebook robust when tools fail or return unexpected data.

Example usage

- After installing dependencies and adding the `.env` file, open `Agent.ipynb` and run cells sequentially in a Jupyter environment (or VS Code notebook view). The key cells initialize the LLM, register tools, create the agent, and run the executor.

Security
- Keep your API keys out of source control. Use `.env` and add it to `.gitignore`.