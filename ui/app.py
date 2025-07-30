import streamlit as st
import sys
import os

# Dynamically add parent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now these imports will work
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from utils.mcp import create_mcp_message

# Initialize agents
ingestion_agent = IngestionAgent()
retrieval_agent = RetrievalAgent()
llm_agent = LLMResponseAgent()

st.title("📄 Agentic RAG Chatbot")

# Upload a document
uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, PPTX, CSV, TXT)", type=["pdf", "docx", "pptx", "csv", "txt", "md"])

# Ask a question
user_question = st.text_input("Ask a question based on the document")

# If both file and question provided
if uploaded_file and user_question:
    with st.spinner("Reading your file and finding answer..."):

        # Step 1: IngestionAgent parses file
        chunks = ingestion_agent.ingest(uploaded_file)

        # Step 2: RetrievalAgent finds top chunks
        top_chunks = retrieval_agent.retrieve(chunks, user_question)

        # Step 3: Message passing using MCP
        message = create_mcp_message(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type_="CONTEXT_RESPONSE",
            payload={
                "top_chunks": top_chunks,
                "query": user_question
            }
        )

        # Step 4: LLMResponseAgent generates answer
        final_answer = llm_agent.generate_response(
            message["payload"]["query"],
            message["payload"]["top_chunks"]
        )

    # Show final answer
    st.subheader("💬 AI Answer:")
    st.write(final_answer)

    # Optional: show retrieved context
    with st.expander("🔍 See retrieved chunks"):
        for chunk in top_chunks:
            st.write(chunk)
