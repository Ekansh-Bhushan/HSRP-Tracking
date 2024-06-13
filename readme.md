# HSRP-Tracking

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Ekansh-Bhushan/HSRP-Tracking/blob/main/LICENSE)

HSRP-Tracking is a Python-based tool for tracking High Security Registration Plates (HSRP) using FastAPI for the backend and web scraping techniques. This project aims to provide a simple and efficient way to monitor the status of HSRP applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **FastAPI Backend**: Utilizes FastAPI for creating the RESTful API.
- **Web Scraping**: Scrapes data from relevant websites to provide up-to-date HSRP status.
- **Asynchronous**: Supports asynchronous operations for efficient handling of multiple requests.
- **Docker Support**: Dockerfile included for containerized deployment.

## Installation

### Prerequisites

- Python 3.8+
- [Docker](https://www.docker.com/get-started) (optional, for containerized deployment)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/Ekansh-Bhushan/HSRP-Tracking.git
    cd HSRP-Tracking
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    uvicorn main:app --reload
    ```

5. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Docker Deployment

1. Build the Docker image:
    ```sh
    docker build -t hsrp-tracking .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 hsrp-tracking
    ```

## Usage

### Local Usage

After starting the application, you can interact with the API using tools like `curl`, Postman, or directly via the browser at `http://127.0.0.1:8000/docs`.

### Example Request

To check the HSRP status, send a GET request to the `/track` endpoint with the required parameters.

```sh
curl -X GET "http://127.0.0.1:8000/track?registration_number=YOUR_REGISTRATION_NUMBER&mobile_number=YOUR_MOBILE_NUMBER"
