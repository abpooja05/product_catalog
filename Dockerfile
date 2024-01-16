# Use the official Python image as the base image
FROM python:3.12

# Set environment variables to prevent Python from writing pyc files and buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
