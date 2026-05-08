# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a RESTful API using the FastAPI framework. You'll create endpoints that accept requests, process data, and return structured responses, understanding the core concepts of web APIs and HTTP methods.

## 📝 Tasks

### 🛠️ Task 1: Create a Simple GET Endpoint

#### Description
Build your first FastAPI application with a basic GET endpoint that returns static data. This will familiarize you with the FastAPI syntax and how to run a server.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Define a GET endpoint at the path `/api/greet` that returns a JSON response
- The response should include a greeting message and a timestamp
- Start the server using `uvicorn` and test the endpoint using a browser or API client

### 🛠️ Task 2: Add Dynamic Endpoints with Request Parameters

#### Description
Extend your API to accept dynamic input from users. Create endpoints that accept query parameters or path parameters and return responses based on the input.

#### Requirements
Completed program should:

- Create a GET endpoint at `/api/users/{user_id}` that accepts a user ID as a path parameter
- Return a JSON object with user information (name, email, user_id)
- Add a GET endpoint at `/api/search` that accepts a query parameter `q` for search terms
- Return a JSON object with search results (or a message if no results found)
- Validate that path parameters are valid types (e.g., integers)

### 🛠️ Task 3: Implement POST Endpoint with Request Body

#### Description
Create a POST endpoint that accepts data from the client and processes it. This involves handling request bodies and sending meaningful responses.

#### Requirements
Completed program should:

- Create a POST endpoint at `/api/tasks` that accepts JSON data (task title and description)
- Validate the request body and ensure required fields are present
- Return a 201 status code with the created task data (including an auto-generated ID)
- Add basic error handling to return a 400 status code for invalid requests
- Test the endpoint using an API client (e.g., Postman, curl, or Python requests library)
