from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configura la clave API de OpenAI usando la variable de entorno.
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    # Renderiza el archivo index.html que se encuentra en la carpeta templates
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Extrae el mensaje del usuario enviado en el cuerpo de la petición
    user_message = request.json.get("message")

    # Llama a la API de OpenAI usando el modelo o3-mini
    response = openai.ChatCompletion.create(
        model="o3-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": user_message},
        ]
    )

    # Extrae y devuelve la respuesta del chatbot
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
