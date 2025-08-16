#!/bin/bash
# A simple CI/CD pipeline script to build and deploy our Flask app
# NOTE: this is for docker automation

# Stop and remove old container if it exists
docker rm -f todo-app

# Build the Docker image
docker build -t todo-app .

# Run the new Docker container
docker run -d -p 5000:5000 --name todo-app todo-app
