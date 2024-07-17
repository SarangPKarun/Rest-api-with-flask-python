# Stores REST API

This is a RESTful API for managing stores, items, and tags. The API allows you to create, read, update, and delete stores, items, and tags. It also allows you to link tags to items.

## Table of Contents

- [Installation](#installation)
  - [Using Docker](#using-docker)
  - [Using Virtual Environment](#using-virtual-environment)
- [Running the API](#running-the-api)
  - [Using Docker](#using-docker-1)
  - [Using Virtual Environment](#using-virtual-environment-1)
- [Testing the API](#testing-the-api)
  - [Using Insomnia](#using-insomnia)
  - [Using Postman](#using-postman)
- [API Endpoints](#api-endpoints)

## Installation

### Using Docker

1. Ensure you have Docker and Docker Compose installed on your machine.

2. Clone the repository:

   ```bash
   git clone https://github.com/SarangPKarun/Rest-api-with-flask-python.git
   cd Rest-api-with-flask-python
   ```

3. Build the Docker image:

   ```bash
   docker-compose build
   ```

### Using Virtual Environment

1. Ensure you have Python 3.8+ and pip installed on your machine.

2. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/stores-api.git
   cd stores-api
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

### Using Docker

1. Start the containers:

   ```bash
   docker-compose up
   ```

2. The API will be accessible at `http://localhost:5000`.

### Using Virtual Environment

1. Set up the database:

   ```bash
   flask db upgrade
   ```

2. Run the application:

   ```bash
   flask run
   ```

3. The API will be accessible at `http://localhost:5000`.

## Testing the API

### Using Insomnia

1. Open Insomnia and create a new request.

2. Set the request URL to `http://localhost:5000/store` (or any other endpoint).

3. Set the method to GET, POST, DELETE, etc., based on the endpoint you are testing.

4. For POST and PUT requests, set the body to JSON and provide the necessary data.

### Using Postman

1. Open Postman and create a new request.

2. Set the request URL to `http://localhost:5000/store` (or any other endpoint).

3. Set the method to GET, POST, DELETE, etc., based on the endpoint you are testing.

4. For POST and PUT requests, set the body to raw and JSON format and provide the necessary data.

## API Endpoints

- `GET /store`: Get all stores.
- `POST /store`: Create a new store.
- `GET /store/<int:store_id>`: Get a store by ID.
- `DELETE /store/<int:store_id>`: Delete a store by ID.
- `GET /store/<int:store_id>/tag`: Get all tags in a store.
- `POST /store/<int:store_id>/tag`: Create a new tag in a store.
- `POST /item/<int:item_id>/tag/<int:tag_id>`: Link a tag to an item.
- `DELETE /item/<int:item_id>/tag/<int:tag_id>`: Unlink a tag from an item.
- `GET /tag/<int:tag_id>`: Get a tag by ID.
- `DELETE /tag/<int:tag_id>`: Delete a tag by ID (if not linked to any items).

Feel free to explore the API using Insomnia or Postman by sending requests to these endpoints. Ensure your requests are correctly formatted and include the necessary headers and body data.
