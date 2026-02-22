from flask import Flask, render_template, request
from core.retriever import semantic_search
from core.llm import generate_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None

    if request.method == "POST":
        query = request.form["question"]

        results = semantic_search(query)

        if not results:
            answer = "I don't know. No relevant content found."
        else:
            top_score = results[0][1]

            if top_score < 0.3:
                answer = "I don't know. No relevant content found."
            else:
                context = [text for text, score in results if score >0.4]
                answer = generate_answer(query, context)

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)