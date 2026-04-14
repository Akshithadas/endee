from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

knowledge = [
    "AI stands for Artificial Intelligence",
    "Python is used for AI development",
    "Neural networks are used in deep learning"
]

vectors = model.encode(knowledge)

question = "What is AI?"
q_vec = model.encode([question])[0]

scores = np.dot(vectors, q_vec)

print("Answer:", knowledge[np.argmax(scores)])
