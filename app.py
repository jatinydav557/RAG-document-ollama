import streamlit as st
import os
import time
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Question: {input}
    """
)

# Vector embedding creation
def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model="all-minilm:latest")  
        st.session_state.loader = PyPDFDirectoryLoader("research_papers")  
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# Streamlit UI
st.set_page_config(page_title="RAG with Groq + Ollama", layout="centered")
st.title("📄 RAG Document Q&A With 🧠 Groq + 🦙 LLaMA3")
st.markdown("Place PDFs inside the `research_papers/` folder and ask questions about them.")

user_prompt = st.text_input("🔍 Enter your query from the research paper:")

if st.button("📚 Build Vector Database"):
    try:
        create_vector_embedding()
        st.success("✅ Vector Database is ready!")
    except Exception as e:
        st.error(f"❌ Failed to process documents: {e}")

if user_prompt:
    if "vectors" not in st.session_state:
        st.warning("⚠️ Please click 'Build Vector Database' before asking questions.")
    else:
        with st.spinner("Thinking..."):
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            start = time.process_time()
            response = retrieval_chain.invoke({'input': user_prompt})
            elapsed = time.process_time() - start

        st.markdown(f"⏱️ Response generated in **{elapsed:.2f} seconds**")
        st.markdown("### 🧠 Answer:")
        st.write(response['answer'])

        with st.expander("📄 Similar Documents"):
            for i, doc in enumerate(response['context']):
                st.markdown(f"**Match {i+1}:**")
                st.write(doc.page_content)
                st.write("---")
