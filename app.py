from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/auth', methods=['GET','POST'])
def auth():
    # Check if the request contains JSON data


# Step 2: Send POST request to obtain Bearer Token
    url = "http://192.168.192.194:2003/symfony/web/index.php/oauth/issueToken"
    payload = {
        "client_id": "chetan",
        "client_secret": "chetan",
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=payload)
    print(response.text)

    return jsonify({'status': 'Success'}), 200


app.run(debug=True)