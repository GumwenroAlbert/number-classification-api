from flask import Flask, request, jsonify

app = Flask(__name__)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def classify_number(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("even" if n % 2 == 0 else "odd")
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify():
    try:
        number = request.args.get('number', type=int)
        if number is None:
            return jsonify({"error": "Invalid number"}), 400
        
        response = {
            "number": number,
            "is_prime": number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)),
            "is_perfect": sum(i for i in range(1, number) if number % i == 0) == number,
            "properties": classify_number(number),
            "digit_sum": sum(int(d) for d in str(number)),
            "fun_fact": f"{number} is {'an Armstrong number' if 'armstrong' in classify_number(number) else 'not an Armstrong number'}."
        }

        return jsonify(response), 200
    except Exception:
        return jsonify({"error": True}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
