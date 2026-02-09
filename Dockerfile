# Use an official Python base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (optional, for documentation/clarity)
EXPOSE 2001

# Command to run the application using Gunicorn and Uvicorn workers
CMD ["gunicorn", "main:app", "--workers", "2", "--timeout", "120", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:2001"]