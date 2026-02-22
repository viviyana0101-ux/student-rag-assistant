# 🎓 Student RAG AI Assistant (SQLite + Flask + Ollama)

A Retrieval-Augmented Generation (RAG) based Student Information Assistant built using:

- 🗄 SQLite (document storage)
- 🤖 Ollama (LLM + embeddings)
- 🔎 Semantic Search (vector similarity)
- 🌐 Flask (Web UI)
- 📁 Text-based data source
- 🔐 Strict grounded answering (No external knowledge)

---

## 📌 Project Overview

This project implements a complete RAG (Retrieval-Augmented Generation) system where:

1. Student information is stored in text files.
2. Data is loaded into SQLite.
3. Embeddings are generated using `nomic-embed-text`.
4. Semantic search retrieves relevant content.
5. `mistral` LLM generates answers ONLY from retrieved context.
6. If no relevant content is found → the assistant responds:
