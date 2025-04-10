# doc_utils.py

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5)
parser = StrOutputParser()

def load_document(file_path):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()

def summarize_document(content):
    prompt = PromptTemplate(
        template="Write a summary for the following document:\n{poem}",
        input_variables=["poem"]
    )
    chain = prompt | model | parser
    return chain.invoke({"poem": content})

def answer_question(content, question):
    prompt = PromptTemplate(
        template="Answer the following question based on the document:\n\nDocument:\n{context}\n\nQuestion: {question}",
        input_variables=["context", "question"]
    )
    chain = prompt | model | parser
    return chain.invoke({"context": content, "question": question})
