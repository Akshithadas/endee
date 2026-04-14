
<p align="center">
  <img src="https://img.shields.io/badge/Endee-Vector_DB-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/AI-Search-green?style=flat-square" />
  <img src="https://img.shields.io/badge/License-Apache_2.0-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
</p>

<p align="center">
  <h1>Endee</h1>
  <p>High-performance open-source vector database for AI search, RAG, semantic search, and hybrid retrieval</p>
</p>

---

## Why Endee

- Built for AI search and retrieval systems  
- Supports vector + hybrid search  
- Optimized for performance workloads  

---

## Features

- High-performance vector search engine  
- Hybrid search (dense + sparse support)  
- Payload filtering for metadata-aware retrieval  
- Scalable architecture for AI workloads  
- Optimized for low-latency search  

---

## Modules

### ai-search
Handles semantic search, query processing, and retrieval logic.

- Documentation: ./ai-search/README.md

---

## Architecture

Endee follows a modular vector search pipeline:

---

## API (Conceptual)
### Search Request
```json
{
  "query": "machine learning",
  "top_k": 5
}
[
  {
    "id": "doc1",
    "score": 0.92,
    "text": "Introduction to machine learning..."
  }
]
---
