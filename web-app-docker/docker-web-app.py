from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route('/docker')

def home():
    return "Hello, cloud ambassadors! Welcome to my Flask app running on Docker!"
    


# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  # Listen on all IPs, port 5000