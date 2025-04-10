# 📄 Document Analyzer (Streamlit + LangChain)

This is a Streamlit-powered app that allows users to upload documents and interact with their contents using LLMs like GPT via LangChain.

## 🚀 Features

- Upload PDFs
- Ask questions about them
- Uses LangChain + OpenAI + Streamlit
- HuggingFace/Google embeddings optional

## 🛠 Setup

```bash
git clone https://github.com/vasujunior7/Documenet-Analyzer.git
cd Documenet-Analyzer
pip install -r requirements.txt
cp .env.example .env  # Then fill in your API keys
streamlit run app.py
