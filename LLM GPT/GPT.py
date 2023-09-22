# import streamlit as st
# from langchain.chat_models import ChatOpenAI
# from langchain.agents import initialize_agent
# from langchain.agents import Tool
# from langchain.tools import  DuckDuckGoSearchRun
# from langchain.tools import YouTubeSearchTool


# llm = ChatOpenAI(model_name= "gpt-3.5-turbo",
#                  openai_api_key="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",
#                  temperature=1)
# search = ()
# search_tool = Tool(
#     name="SEARCH-DUCK",
#     description="Search Google for recent results.",
#     func=DuckDuckGoSearchRun.run)

# yt = YouTubeSearchTool()
# yt_tool = Tool(
#     name="youtube",
#     description="yt_search",
#     func=yt.run
# )
# tools=[search_tool,yt_tool]


# agent = initialize_agent(tools=tools,
#                          llm=llm,
#                          agent='zero-shot-react-description',
#                          verbose=True)


# st.title('Subha\'s Agent\'s reply')
# prompt=st.text_input("get yo! prompt here!")

# if prompt:
#     response=agent.run(prompt)
#     st.write(response)

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import YouTubeSearchTool
from langchain.agents import AgentType


llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                 openai_api_key="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",
                 temperature=1)


search_tool = Tool(
    name="SEARCH-DUCK",
    description="Search DuckDuckGo for recent results.",
    func=DuckDuckGoSearchRun.run  
)

yt_tool = Tool(
    name="youtube",
    description="yt_search",
    func=YouTubeSearchTool.run
)

tools = [search_tool, yt_tool]

agent = initialize_agent(tools=tools,
                         llm=llm,
                         #agent='subhas_agent',
                         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

st.title("Agent's replies yo!")
prompt = st.text_input("Enter your prompt here!")

if prompt:
    response = agent.run(prompt)
    st.write(response)