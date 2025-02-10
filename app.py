from flask import Flask, request, jsonify

app = Flask(__name__)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route that you will 
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Number Classification API!',
        'status': 'success'
    }), 200
    return jsonify(response), 200
# Existing routes for your API
@app.route('/classify', methods=['POST'])
def classify_number():
    # Your existing logic for classifying numbers
    return jsonify({"result": "classified number"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    response = {
        "message": "Welcome to the Number Classification API!",
        "status": "success"
    }
    return jsonify(response), 200

@app.route('/classify', methods=['GET'])
def classify_number():
    try:
        number = request.args.get("number", type=int)
        if number is None:
            return jsonify({"error": "Missing 'number' parameter"}), 400
        
        classification = "even" if number % 2 == 0 else "odd"

        response = {
            "number": number,
            "classification": classification
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
