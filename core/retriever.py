import sqlite3
import pickle
import numpy as np
from core.embeddings import get_embedding

def semantic_search(query, top_k=30):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    query_embedding = get_embedding(query)

    cursor.execute("SELECT doc_id, embedding FROM document_embeddings")
    rows = cursor.fetchall()

    scores = []

    for doc_id, blob in rows:
        doc_embedding = pickle.loads(blob)
        similarity = np.dot(query_embedding, doc_embedding)
        scores.append((doc_id, similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    top_docs = scores[:top_k]

    results = []

    for doc_id, score in top_docs:
        cursor.execute("SELECT content FROM documents WHERE id = ?", (doc_id,))
        row = cursor.fetchone()
        if row:
            results.append((row[0], score))

    conn.close()
    return results