from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()
app = Flask(__name__)
# Set the secret as an environment variable before running the app
# Access variables using os.getenv()
variable_value = os.getenv("MY_SECRET_KEY")

@app.route('/')
def hello_world():
    return '<h1>Hello, GitHub! From Elie</h1>'

# POST endpoint to receive GitHub webhook events
@app.route('/hook', methods=['POST'])
def github_webhook():
    data = request.get_json()

    if data:
        print("Received GitHub webhook payload:")
        print(data)
        return "Webhook received successfully!"
    else:
        return "No data received."

# POST endpoint to receive and print POST data
@app.route('/receive_post_data', methods=['POST'])
def receive_post_data():
    data = request.get_json()  # assuming JSON data in the POST request
    print(f"Received POST data: {data}")
    return "POST data received successfully!"

# GET endpoint to provide a sample response with a secret from the environment variable
@app.route('/sample_get_endpoint', methods=['GET'])
def sample_get_endpoint():
    # Fetch the secret from the environment variable
    secret_key = os.environ.get("MY_SECRET_KEY", "default_secret")

    response = {"message": "Hello, this is a sample GET endpoint!", "secret_key": secret_key}
    return jsonify(response)

if __name__ == '__main__':
    # Bind to '0.0.0.0' to make it accessible externally
    # Use a specific port, for example, 5000
    app.run(host='0.0.0.0', port=8000, debug=True)
