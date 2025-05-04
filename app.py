import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()

arxiv_wrapper=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=wiki_wrapper)
search=DuckDuckGoSearchRun(name="Search")
st.title("Langchain chat with search")
st.sidebar.title("settings:")
api_key=st.sidebar.text_input("enter your groq api key",type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi I am a chatbot who search the web.How can I help you?"}
    ]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

    

if prompt:=st.chat_input(placeholder="what is machine Learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    if api_key:
        llm=ChatGroq(groq_api_key=api_key,model_name="gemma2-9b-it",streaming=True)
        tools=[arxiv,search,wiki]
        search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parse_errors=True)
        with st.chat_message("assistant"): 
             st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
             response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
             st.session_state.messages.append({'role':'assistant','content':response})
             st.write(response)

       

        

        

    
    






