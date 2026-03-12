from flask import Flask, render_template, request, jsonify
from questions import questions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/quiz", methods=["GET"])
def quiz():
  return render_template("quiz.html", questions=questions, total=len(questions))

@app.route("/check-answer", methods=["POST"])
def check_answer():
  data = request.get_json()
  question_index = data.get("question_index")
  user_answer = data.get("answer")
  
  if question_index < 0 or question_index >= len(questions):
    return jsonify({"error": "Pergunta inválida"}), 400
  
  q = questions[question_index]
  is_correct = user_answer == q["answer"]
  
  return jsonify({
    "correct": is_correct,
    "correct_answer": q["answer"],
    "explanation": q["explanation"]
  })

@app.route("/results")
def results():
  score = request.args.get("score", 0, type=int)
  total = request.args.get("total", len(questions), type=int)
  return render_template("result.html", score=score, total=total)

if __name__ == "__main__":
  app.run(debug=True)