from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load model (this may take a moment at first run)
qa_pipeline = pipeline("question-answering")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    passage = request.form.get("passage")
    question = request.form.get("question")

    print("Question:", question)
    print("Passage:", passage)

    try:
        result = qa_pipeline(question=question, context=passage)
        print("Answer:", result["answer"])
        return jsonify({"answer": result["answer"]})
    except Exception as e:
        print("Error:", e)
        return jsonify({"answer": "Error processing the input."})

if __name__ == "__main__":
    app.run(debug=True)
