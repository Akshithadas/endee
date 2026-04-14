from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

docs = [
    "AI improves automation",
    "Machine learning is part of AI",
    "Deep learning uses neural networks"
]

doc_vecs = model.encode(docs)

query = "What is machine learning?"
q_vec = model.encode([query])[0]

scores = np.dot(doc_vecs, q_vec)

print("Best Match:", docs[np.argmax(scores)])
