# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to start the application
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]

