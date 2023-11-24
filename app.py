from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    try:
        # Get the JSON data from the request
        data = request.json

        # Your processing logic here
        # For example, let's just return the received data
        return jsonify({"result": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
