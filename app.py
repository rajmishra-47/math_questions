from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data when the server starts
with open('data.json', 'r') as f:
    questions_data = json.load(f)

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions_data)

if __name__ == '__main__':
    app.run(debug=True)
