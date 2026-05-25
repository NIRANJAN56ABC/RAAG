from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "FastAPI is used to build APIs."
]

embeddings = model.encode(documents)

def retrieve(query: str, k=1):
    query_embedding = model.encode([query])[0]

    scores = np.dot(embeddings, query_embedding)

    top_k_idx = np.argsort(scores)[-k:][::-1]

    results = [documents[i] for i in top_k_idx]

    return "\n".join(results)