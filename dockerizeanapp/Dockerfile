# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Run the Python script when the container starts
CMD ["python", "hello.py"]

# docker build -t my-hello-app .
# docker run my-hello-app
