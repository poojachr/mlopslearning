# Use the official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy the Python script into the container
COPY model.py .

# Command to run the script
CMD ["python", "model.py"]
