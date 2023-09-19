# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set up a working directory
WORKDIR /app

# Install necessary dependencies
RUN pip install transformers uvicorn fastapi

# Install TensorFlow 2.0
# RUN pip install tensorflow

# Install PyTorch
RUN pip install torch torchvision torchaudio

# Copy your inference script into the container
COPY ./inference_app.py /app/inference_app.py

# Expose the port for the FastAPI server
EXPOSE 8000

# Define the command to start the FastAPI server
CMD ["uvicorn", "inference_app:app", "--host", "0.0.0.0", "--port", "8000"]
