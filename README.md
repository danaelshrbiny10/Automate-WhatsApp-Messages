# Automate-WhatsApp-Messages

[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=yellow&color=darkblue)](https://www.python.org) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  [![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-brown)](http://www.pydocstyle.org/en/stable/) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-pink?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This project aims to provide a way to automate sending WhatsApp messages to contacts and groups using Python.

## Table of Contents

- [installation](./README.md/#installation)
- [usage](./README.md/#usage)
- [API Documentation](./README.md/#api-documentation)
- [Database Backend](./README.md/#database-backend)
- [Authentication](./README.md/#jwt-authentication)
- [technologies](./README.md/#technologies)
- [License Information](./README.md/#license-information)

## Installation

To get started with the Automate-WhatsApp-Messages project:

1. Clone the repository to your local machine

```bash
git clone https://github.com/danaelshrbiny10/Automate-WhatsApp-Messages.git
```

2. Create a virtual environment and activate it:

```bash
# install virtual enviroment
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
venv/source/activate

```

3. Install the project dependencies:

```bash
pip install -r requirements.txt

```

## run project

```bash
python manage.py runserver
```

## Usage

You can use this [postman collection](https://www.postman.com/science-saganist-7786711/workspace/whatsapp-api/collection/13841690-010abb84-a671-4e85-9f60-a057728c6915?action=share&creator=13841690) to learn more about the API usage

## API Documentation

The API endpoints are documented using Swagger. To access the API documentation:

1. Start the development server

```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000/` or `http://localhost:8000/redoc/`

## Database Backend

use PostgreSQL and update the DATABASES settings in `ecommerce/settings.py` with your PostgreSQL database configuration.

```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "Whatsapp API",
        "USER": "postgres",
        'PASSWORD': 'your_db_password',
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

```

## JWT Authentication

This project uses JWT (JSON Web Token) authentication for user authentication. JWT is a widely adopted standard for securing API endpoints and provides a stateless mechanism for authentication and involves the following components:

1. Token-Based Authentication: Instead of traditional session-based authentication, JWT authentication relies on tokens. When a user logs in or registers, a JWT token is generated and returned to the client.
2. Token Verification: On subsequent requests, the client includes the JWT token in the request headers to authenticate itself. The server verifies the token to authenticate and authorize the user.
3. Token Expiration: JWT tokens have an expiration time, typically set to a short duration for security reasons. Once expired, the token is no longer valid and the client needs to obtain a new token.

To authenticate requests using JWT tokens, include the token in the request headers. The token should be included in the Authorization header using the Bearer scheme

```bash
Bearer <jwt-token>
```

## Technologies

The application is built with the following technologies:

- Django
- Django Rest Framework
- Docker
- Docker Compose
- Nginx

## License Information

This project is licensed under the MIT License. For more details, see the LICENSE file.
