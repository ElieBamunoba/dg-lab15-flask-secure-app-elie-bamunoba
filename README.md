
# Flask Web App with GitHub Webhooks

This Flask web application demonstrates how to receive GitHub webhook events and handle POST requests. It also showcases loading environment variables from a `.env` file using `python-dotenv`.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (version 3.x)
- Flask
- python-dotenv

You can install the required packages using pip:

```bash
pip install flask python-dotenv
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/deployguru-learning/dg-lab15-flask-secure-app-elie-bamunoba.git

cd dg-lab15-flask-secure-app-elie-bamunoba
```

2. Create a `.env` file in the root directory and add your secret key:

```plaintext
MY_SECRET_KEY=your_secret_key_here
```

3. Run the Flask app:

```bash
python app.py
```

4. Access the app in your browser at `http://localhost:8000`.

## Endpoints

- `/`: Displays a simple message.
- `/hook`: Endpoint to receive GitHub webhook events.
- `/receive_post_data`: Endpoint to receive and print POST data.
- `/sample_get_endpoint`: Provides a sample response with a secret from the environment variable.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


## Contact
For any issues or questions, please contact Elie at eliebamunoba@gmail.com


