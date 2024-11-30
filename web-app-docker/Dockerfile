# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app code into the container
COPY docker-web-app.py /app/

# Install Flask
RUN pip install flask

# Expose port 5000 for the Flask app
EXPOSE 8000

# Run the Flask app
CMD ["python", "docker-web-app.py"]