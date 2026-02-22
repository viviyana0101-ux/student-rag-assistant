from core.retriever import semantic_search
from core.llm import generate_answer

def main():
    print("Student AI Assistant")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        results = semantic_search(query)

        if not results:
            print("I don't know. No relevant content found.\n")
            continue

        top_score = results[0][1]

        # Confidence threshold
        if top_score < 0.3:
            print("I don't know. No relevant content found.\n")
            continue

        context = [text for text, score in results]

        answer = generate_answer(query, context)

        print("\n", answer, "\n")

if __name__ == "__main__":
    main()