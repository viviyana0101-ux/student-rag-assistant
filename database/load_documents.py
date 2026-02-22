import os
import sqlite3
import pickle
from core.embeddings import get_embedding

def load_documents():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    # Clear old data
    cursor.execute("DELETE FROM documents")
    cursor.execute("DELETE FROM document_embeddings")

    data_folder = "data"

    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(data_folder, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            title = filename.replace(".txt", "")

            cursor.execute(
                "INSERT INTO documents (title, content) VALUES (?, ?)",
                (title, content)
            )

    conn.commit()

    # Generate embeddings
    cursor.execute("SELECT id, content FROM documents")
    rows = cursor.fetchall()

    for doc_id, content in rows:
        embedding = get_embedding(content)
        blob = pickle.dumps(embedding)

        cursor.execute(
            "INSERT INTO document_embeddings (doc_id, embedding) VALUES (?, ?)",
            (doc_id, blob)
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_documents()
    print("Documents loaded and embeddings created.")