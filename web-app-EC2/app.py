from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route('/')

def home():
    return "Hello, cloud ambassadors! Welcome to my Flask app running on EC2!"
    


# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Listen on all IPs, port 5000