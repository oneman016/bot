from flask import Flask, render_template, request, jsonify
import openai  # Import OpenAI library

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if 'message' in request.json:
        user_message = request.json["message"]
        if user_message.strip() == "":
            return jsonify({"error": "Empty message"}), 400
        # Use OpenAI's GPT-2 to generate a response
        bot_response = openai.Completion.create(
            engine="davinci",  # Change the engine to 'davinci'
            prompt=user_message,
            max_tokens=50
        ).choices[0].text.strip()
        return jsonify({"message": bot_response})
    else:
        return jsonify({"error": "message key not found in request"}), 400

if __name__ == "__main__":
    app.run(debug=True)
