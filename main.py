from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Configura tu API Key
client = Groq(api_key="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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Responde siempre en español de forma clara y concisa."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
        )
        respuesta = completion.choices[0].message.content
        return jsonify({"response": respuesta})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)