from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import  YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

##web search agent
web_Search_agent=Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=("Always include sources"),
    show_tool_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

## multi ai agent
multi_ai_agent=Agent(
    team=[web_Search_agent, finance_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommnedation and share the latest news for NVDA", stream=True)