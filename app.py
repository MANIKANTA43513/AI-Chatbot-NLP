from flask import Flask, render_template, request, jsonify
from chatbot_pro import scrape_website, chunk_data, create_vector_db, search, format_answer

app = Flask(__name__)

# Load once
url = "https://botpenguin.com/"
data = scrape_website(url)
chunks = chunk_data(data)
vectorizer, vectors = create_vector_db(chunks)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"]
    results = search(user_input, chunks, vectorizer, vectors)
    answer = format_answer(results)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)