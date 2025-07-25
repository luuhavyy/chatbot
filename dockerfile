# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run your main script
CMD ["python", "main.py"]
