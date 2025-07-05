
# 🚀 Flask Calculator App (Dockerized)

## Project Overview

This is a small study project to help me understand how back-end applications interact with front-end components and how applications connect to data pipelines and databases.

It’s a simple web-based calculator API built with **Flask** and **PostgreSQL**, containerized using **Docker** and orchestrated with **Docker Compose**.

---

## Features

✅ Accepts numeric inputs via URL query parameters  
✅ Performs addition of two numbers  
✅ Stores each calculation and result in a Postgres table as a permanent ledger  
✅ Runs entirely in Docker containers

---

## Tech Stack

- Python (Flask)
- PostgreSQL
- Docker + Docker Compose
- psycopg2 for database connectivity

---

## How It Works

- **Flask App Container**
  - Exposes endpoints:
    - `/` → Home page
    - `/calculate` → Accepts two numbers and returns the result as JSON
  - Connects to Postgres to store each calculation as a record in a ledger

- **Postgres Container**
  - Contains a table named `calculations` with columns:
    - `num_1`
    - `operation`
    - `num_2`
    - `result`

- **Docker Compose**
  - Spins up both containers and networks them together

---

## Usage

### Prerequisites

- Docker
- Docker Compose

---

### Run the App

Clone the repo and navigate into the directory:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
2. Start the containers:
```
docker-compose up --build
```
3. Visit the app in your browser:
```
http://localhost:5050/
```
4. Call the `/calculate` route with two query parameters:
```
http://localhost:5050/calculate?num_1=5&num_2=3
```
- Example JSON response:
```
{
  "num_1": 5.0,
  "operation": "addition",
  "num_2": 3.0,
  "result": 8.0
}
```
## Planned Next Steps
-   Add more arithmetic operations (e.g. subtraction, multiplication)
-   Improve error handling and edge-case coverage
-   Add unit tests
-   Explore adding a simple frontend UI to interact with the API
- Store 'historic' calculation in Postgres with a timestamp to denote when the calculation was performed
    

## Why I Built This

I built this project because I wanted to:

-   Understand how back-end APIs serve data to potential front-end applications
-   Explore how applications connect to databases and store persistent data
-   Understand how Docker works
-   Get hands-on with Python web frameworks and SQL interactions


## Status

> ⚠️ **Note:** This project is still a work in progress. It’s not production-ready yet but demonstrates multi-container architecture and Python-Postgres interactions.
