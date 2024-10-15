# Flask CMS

This is a personal blog CMS built using Flask, MongoDB, Marshmallow for serialization, and Swagger for API documentation.

## Features

- Uses **Flask** for the web framework.
- **MongoDB** for the database, with support for **mongomock** during testing.
- **Marshmallow** for data validation and serialization.
- API documentation using **Swagger**.
- Unit tests with **pytest**.

## Project Structure
```
flask_cms/
|
├── app/
│   ├── controllers/          # Business logic and interaction with models
│   ├── docs/                 # Swagger YAML files for API documentation
│   ├── helpers/              # Utility functions for reusability
│   ├── routes/               # Flask routes/endpoints
│   ├── schemas/              # Marshmallow schemas for serialization and validation
│   ├── services/             # MongoDB services
│   ├── __init__.py           # Application factory, config, and database setup
|
├── tests/                    # Unit tests
│   ├── conftest.py           # Pytest fixtures for testing
|
├── config.py                 # Application configurations (development, testing, production)
├── requirements.txt          # List of dependencies
├── .gitignore                # Files and directories to be ignored by git
├── README.md                 # Project documentation
├── pytest.ini                # Pytest configuration file
├── .env.example              # Example environment variables file
```

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB
- Flask
- Virtual Environment (recommended)

### Setup

1. Install the dependencies:
```shell
pip install -r requirements.txt
```

2. Set up environment variables by creating a `.env` file at the root:
```shell
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/mydatabase
```

3. Run the Flask application:
```shell
flask run
```
4. Access the Swagger documentation at:

http://localhost:5000/apidocs

## Running Tests

Unit tests are written using **pytest** and **mongomock**. To run the tests:
```shell
pytest -v
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
