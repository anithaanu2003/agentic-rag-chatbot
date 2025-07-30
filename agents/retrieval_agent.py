from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalAgent:
    def __init__(self):
        # Load sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunks = []

    def build_index(self, chunks):
        # Store chunks and create embeddings
        self.chunks = chunks
        embeddings = self.model.encode(chunks)
        embeddings = np.array(embeddings).astype("float32")

        # Build FAISS index
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def retrieve(self, chunks, query, top_k=3):
        # Build index from chunks
        self.build_index(chunks)

        # Encode the user query
        q_embedding = self.model.encode([query])
        q_embedding = np.array(q_embedding).astype("float32")

        # Search top_k similar chunks
        D, I = self.index.search(q_embedding, top_k)
        return [self.chunks[i] for i in I[0]]
