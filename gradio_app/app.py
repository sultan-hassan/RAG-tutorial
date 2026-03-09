import os
from datasets import load_dataset
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import gradio as gr

# Load environment variables from .env file
load_dotenv()
groq_key = os.environ.get('groq_api_keys')
# Initialize LLM
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_key)

print("✅ Setup complete. API Key loaded.")


# Load data from huggingface for astro arxiv papers
ds = load_dataset("mehnaazasad/arxiv_astro_co_ga")
data = ds["test"]["abstract"][:20] # take first examples


# 1. Initialize the Embedding Model (Converts text to math)
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Create and Populate Vector Store
vectorstore = Chroma(
    collection_name="dataset_store",
    embedding_function=embed_model,
    persist_directory="./chroma_db",
)


vectorstore.add_texts(data)
retriever = vectorstore.as_retriever()



print("🧠 Vector Store created. The AI can now 'search' your data.")


template = """You are astronomy expert. 
Use the provided context to answer the question. 
If you don't know, say you don't know. Explain in detail.
Context: {context}
Question: {question}
Answer:"""

rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)
print("⛓️ RAG Chain is ready.")

def rag_memory_stream(text):
    partial_text = ""
    for new_text in rag_chain.stream(text):
        partial_text += new_text
        yield partial_text

demo = gr.Interface(
    title="Real-time Astronomy AI Assistant",
    fn=rag_memory_stream,
    inputs="text",
    outputs="text",
    examples=['what are the characteristics of blue compact dwarf?', 'What is cold dark matter?'],
)


demo.launch()
