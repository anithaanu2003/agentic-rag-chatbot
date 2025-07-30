# 🧠 Agentic RAG Chatbot with MCP (Multi-Format Document QA)

This project is a multi-format document Question Answering (QA) chatbot built using an **Agent-based Retrieval-Augmented Generation (RAG)** architecture. It uses **Model Context Protocol (MCP)** for message passing between agents.

## 📂 Supported Document Formats

- PDF
- DOCX (Word)
- PPTX (PowerPoint)
- CSV
- TXT / Markdown

## 🧠 Architecture (Agentic)

- **IngestionAgent** → Parses and splits documents into chunks
- **RetrievalAgent** → Embeds and finds relevant chunks using FAISS + SentenceTransformers
- **LLMResponseAgent** → Uses HuggingFace QA model to answer user query
- **MCP (Model Context Protocol)** → All communication is via structured messages like:
  ```json
  {
    "sender": "RetrievalAgent",
    "receiver": "LLMResponseAgent",
    "type": "CONTEXT_RESPONSE",
    "payload": {
      "top_chunks": [...],
      "query": "What are the KPIs?"
    }
  }
