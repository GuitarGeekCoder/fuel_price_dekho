# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

COPY . /app
# Copy the requirements file into the container
COPY requirement.txt .

# Install the necessary packages
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire Django project into the container
COPY . .

# Collect static files (if you have any)
RUN python manage.py

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the port your app runs on
EXPOSE 8000

# Command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]