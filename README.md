# Setup

This project is a Django REST Framework (DRF) backend application that uses Docker and Docker Compose for easy setup and management. Follow the instructions below to get started.

## Prerequisites

Ensure that you have the following installed on your local machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hicarlodacuyan/meddicc-exam-backend.git   
   cd meddicc-exam-backend
   ```

2. **Create a `.env` file:**

   Create a `.env` file in the root directory of the project based on .env.example

3. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build -d
   ```

4. **Run database migrations:**

   ```bash
   docker exec -it <backend-container-name> python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   docker exec -it <backend-container-name> python manage.py createsuperuser
   ```

6. **Access the API:**

   Import the `Insomnia.json` file in the root directory of the project to your Insomnia app and start using the APIs  

