# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ /app/

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the application
CMD ["python", "-u", "app.py"]
