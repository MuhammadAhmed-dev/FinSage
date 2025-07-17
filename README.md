# 💸 FinSage – Multi-Agent Finance AI

**FinSage** is a multi-agent AI system built with [Phi](https://github.com/Prompt-Engineering-Hub/phi) that helps you get real-time answers to finance-related questions by scraping live data from the web and financial sources.

## 🚀 Features

* 🧠 **Multi-Agent Setup**
  Combines different specialized agents to improve accuracy and response quality.

* 🌐 **Web Search Agent**
  Uses DuckDuckGo to fetch real-time info from the web.
  Always includes sources for transparency.

* 📊 **Finance Agent**
  Uses Yahoo Finance to pull:

  * Live stock prices
  * Analyst recommendations
  * Company fundamentals
  * Latest financial news
    Responses are shown using tables for easy reading.

## 🔧 Tech Stack

* [Phi Framework](https://github.com/Prompt-Engineering-Hub/phi)
* [Groq](https://groq.com/) running LLaMA 3 70B
* `DuckDuckGo` for web search
* `YFinanceTools` for real-time stock data
* `.env` for secure API key management (OpenAI key required for some tools)

## 📦 Installation

```bash
pip install phi
```

Make sure you have a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=your_key_here
```

## 🧪 Example Usage

```python
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA",
    stream=True
)
```

## 📍 Note

This is an experimental project and may require tweaks based on the tools' API limits or model changes.
oo!
