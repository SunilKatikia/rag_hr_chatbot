from flask import Flask, request, jsonify
from rag_engine import get_answer
from firestore_utils import save_session # Basic CRUD for history

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def chat():
    data = request.json
    query = data.get("query")
    history = data.get("history", "") # Retrieve from Firestore in prod
    
    result = get_answer(query, history)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)