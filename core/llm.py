import ollama

def generate_answer(query, context_chunks):

    context_text = "\n\n".join(context_chunks)

    prompt = f"""
You are a student information assistant.

You must answer ONLY using the provided context.
If the answer is not present in the context, reply exactly:
"I don't know. No relevant content found."

Context:
{context_text}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]