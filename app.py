from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_json():
    # Check if the request contains JSON data
    if request.is_json:
        # Parse the JSON data
        data = request.get_json()
        
        # Check if 'text' key exists in the parsed JSON data
        if 'text' in data:
            text = data['text']
            print(text)
        else:
            return jsonify({'error': 'Invalid JSON format: missing "text" key'}), 400

    return jsonify({'error': 'Success'}), 200


app.run(debug=True)