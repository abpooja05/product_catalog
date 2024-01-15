This README provides information on setting up and using your Django project with Docker.

# Django Multicontainer-Docker Project

This is a Django project with multicontainer setup using Docker.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Docker Compose](#docker-compose)
- [Dockerfile](#dockerfile)
- [Contributing](#contributing)

## Prerequisites
Make sure you have the following installed on your machine:
- Docker: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2.Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install project dependencies:
pip install -r requirements.txt

4.Create a .env file and set your environment variables:
SECRET_KEY=your-secret-key
DEBUG=True
MONGO_DB_NAME=productdb
MONGO_DB_HOST=mongo
MONGO_DB_PORT=27017

5.Apply Django migrations:
python manage.py migrate

6.Run the Django development server:
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

7.Docker Compose
Use Docker Compose to orchestrate the multicontainer setup:
docker-compose up --build
Visit http://127.0.0.1:8000/ in your browser.

8.Dockerfile
The project includes a Dockerfile for containerization. To build and run the Docker image:
docker build -t your-image-name .
docker run -p 8000:8000 your-image-name

9.Contributing
Fork the repository and submit a pull request.
