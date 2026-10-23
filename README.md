# Python API Security Client

A beginner-friendly Python project demonstrating safer API client
practices, including environment variables, `.env` configuration,
request headers, timeouts, and error handling.

## Features

-   Loads configuration from a `.env` file using `python-dotenv`
-   Keeps configuration values out of the source code
-   Sends a GET request to retrieve a post from JSONPlaceholder
-   Demonstrates a custom request header
-   Uses a request timeout and `raise_for_status()`
-   Handles common request, HTTP, timeout, JSON, and input errors
-   Validates the post ID before making the request

## Tech Stack

-   Python 3
-   `requests`
-   `python-dotenv`
-   JSONPlaceholder demo API

## Project Structure

``` text
day2_api_security/
├── main.py
├── .env
├── .gitignore
└── README.md
```

**Security note:** `.env` is a local configuration file and should not
be committed to Git. The `.gitignore` file excludes it from normal Git
tracking when it has not already been tracked.

## Setup

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username:

``` bash
git clone https://github.com/YOUR-USERNAME/day2-api-security.git
cd day2-api-security
```

### 2. Create and activate a virtual environment

On macOS or Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install requests python-dotenv
```

### 4. Create your `.env` file

Create a file named `.env` in the project directory:

``` dotenv
APP_NAME=QueryMind AI
API_BASE_URL=https://jsonplaceholder.typicode.com
DEMO_API_KEY=test_key_123
```

These are demonstration values, not real credentials. Do not put real
API keys in source code or commit them to Git.

### 5. Run the program

``` bash
python main.py
```

Enter a post ID from `1` to `100` when prompted.

## Important Learning Note

This project uses JSONPlaceholder, a public testing API. It does **not**
require or validate the `X-Demo-Key` header. The header is included only
to demonstrate how a client can send a header. For real authentication,
follow the specific API provider's documentation.

## Security Practices Demonstrated

-   Read configuration from environment variables
-   Keep `.env` out of version control
-   Set request timeouts
-   Check HTTP status codes with `raise_for_status()`
-   Handle expected request errors
-   Validate user input

If a real API key is accidentally exposed, revoke or rotate it
immediately. Removing a key from the latest version of a file may not
remove it from Git history.

## What I Learned

-   How APIs use requests and responses
-   How to make GET requests with Python
-   How to load configuration using `python-dotenv`
-   How request headers work
-   How to handle HTTP and network errors
-   How to use `.gitignore` to help protect local secrets

## Future Improvements

-   Add unit tests
-   Use a real API that supports authentication
-   Add structured logging
-   Move API logic into a reusable client class
-   Add more endpoints and support for query parameters

------------------------------------------------------------------------

**Learning project:** Week 4 --- Day 2, Python API Security.
