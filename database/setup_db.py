import sqlite3

def setup_database():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS document_embeddings (
        doc_id INTEGER,
        embedding BLOB
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database created successfully.")