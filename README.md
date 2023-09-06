# GIC CodeToImpact Team 5 README

## Introduction

Welcome to our multi-container app repository! This repository contains a collection of microservices designed to work together seamlessly to power our application. Additionally, we have a "common" folder at the root of the directory that stores essential database connection and model information shared across the microservices.

## Table of Contents

- [GIC CodeToImpact Team 5 README](#gic-codetoimpact-team-5-readme)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Setting Up](#setting-up)
  - [Running the App](#running-the-app)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

Before you dive into the code, here's what you need to know to get started with our multi-container app.

## Project Structure

Our project is organized as follows:


```
codetoimpact-team5
├─ analytics
│  ├─ Dockerfile
│  ├─ __init__.py
│  ├─ requirements.txt
│  └─ src
│     ├─ __init__.py
│     ├─ (other files and folders)
│     └─ main.py
├─ common
│  ├─ __init__.py
│  ├─ database.py
│  └─ models.py
├─ entity
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ src
│     ├─ __init__.py
│     ├─ (other files and folders)
│     └─ main.py
├─ genai
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ src
│     ├─ __init__.py
│     ├─ (other files and folders)
│     └─ main.py
├─ ingestor
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ src
│     ├─ __init__.py
│     ├─ (other files and folders)
│     └─ main.py
└─ positions
   ├─ Dockerfile
   ├─ requirements.txt
   └─ src
│     ├─ __init__.py
│     ├─ (other files and folders)
│     └─ main.py

```


- `common/`: This directory contains shared database connection and model information that is used across multiple microservices.

- `ingestor/`, `entity/`, `positions/`, `analytics/`, `genai/`: Each subdirectory represents a microservice with specific functionality. They contain a `requirements.txt` file listing required dependencies, a `Dockerfile` for Docker containerization, and an `src` folder with microservice-specific source code. The `src` folder includes both `__init__.py` and `main.py` files.

## Setting Up

To set up the development environment for our app, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/gic-codetoimpact-team5/codetoimpact-team5.git
cd codetoimpact-team5
```

2. (Optional: if you are planning to run without Docker) Install the required dependencies for each microservice by running the following commands in each microservice's directory:

```
cd ingestor/
pip install -r requirements.txt
```

Repeat the above step for each microservice.

3. Set up any necessary environment variables or configuration files. Refer to the documentation in each microservice's `src` directory for guidance.

## Running the App

To run our multi-container app, follow these general steps:

1. Navigate to the root of the project directory:

```
cd codetoimpact-team5/
```

2. Start each microservice individually by building and running the Docker container using the provided `Dockerfile` in each microservice's directory. Replace `MICROSERVICE_NAME` with the name of the microservice you want to build.

```
docker build -f &lt;microservice_name&gt;/Dockerfile -t <docker_hub_username>/<image_name>:<image_tag>
```

- `MICROSERVICE_NAME`: Replace this with the name of the microservice you want to build (e.g., `genai`).
- `YOUR_DOCKER_HUB_USERNAME`: Replace this with your Docker Hub username or the container registry you're using.
- `YOUR_IMAGE_NAME`: Replace this with the name you want to give to your microservice's Docker image (e.g., `genai-service`).
- `1.0.0`: This is the version tag for the Docker image. You can use a specific version or tag that suits your needs.

Repeat the above step for each microservice you want to run.

3. Ensure that any dependencies specified in each microservice's README are installed and configured correctly.

4. The microservices should work together seamlessly to provide the full functionality of the application.

For example, to build the Docker image for the `genai` microservice, you can run:

```
docker build -f genai/Dockerfile -t <your_username>/genai-service:1.0.0 .
```

