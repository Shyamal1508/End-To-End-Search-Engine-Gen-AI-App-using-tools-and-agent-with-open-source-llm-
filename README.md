# 🔍 End-To-End Search Engine Gen-AI App using Tools and Agent with Open-Source LLM

This project demonstrates how to build a fully functional Generative AI-powered search engine using open-source LLMs, tool-augmented agents, and the LangChain framework. The app supports answering complex queries by retrieving information from multiple sources like Wikipedia, Arxiv, and more — all within a chat interface powered by Streamlit.

---

## ✨ Features

- 🔗 **LangChain Agents & Tools**: Dynamically route queries through different APIs like Wikipedia and Arxiv.
- 🧠 **Open-Source LLM Integration**: Utilizes Hugging Face models instead of proprietary APIs (e.g., OpenAI).
- 💬 **Chat-Based UI**: Built using Streamlit for interactive and intuitive user experience.
- 📚 **Multi-Source Search**: Combines responses from multiple tools to generate insightful answers.
- 🧪 Modular & Extendable Codebase: Easily plug in new tools, models, or search APIs.

---

## 📦 Tech Stack

- **[LangChain](https://python.langchain.com/)**: Framework for building applications with LLMs.
- **[Streamlit](https://streamlit.io/)**: UI framework for interactive Python apps.
- **Tools**:
  - `WikipediaAPIWrapper`
  - `ArxivAPIWrapper`

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Shyamal1508/End-To-End-Search-Engine-Gen-AI-App-using-tools-and-agent-with-open-source-llm.git
cd End-To-End-Search-Engine-Gen-AI-App-using-tools-and-agent-with-open-source-llm


Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Run the App
streamlit run app.py

├── app.py                   # Main Streamlit app
├── README.md                # Project documentation
