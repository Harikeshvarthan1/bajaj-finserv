from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json  # Directly access request.json

        # Separate numbers and alphabets
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [x for x in alphabets if x.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  
            "email": "john@xyz.com",  
            "roll_number": "ABCD123",  
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
