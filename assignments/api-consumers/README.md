# 📘 Assignment: API Consumers with JavaScript

## 🎯 Objective

Use JavaScript to fetch data from a REST API and display dynamic content in a browser. This exercise helps you connect a web front end to a backend service and handle real API responses.

## 📝 Tasks

### 🛠️ Task 1: Fetch User Data

#### Description
Build a function named `fetchUser()` that sends a GET request to a REST API endpoint and displays the result on the page.

#### Requirements
Completed program should:

- Use the Fetch API to request user data from `/api/users/1`
- Convert the JSON response into a JavaScript object
- Display the user name, email, and user ID on the page
- Show an error message if the request fails

### 🛠️ Task 2: Fetch and Render a Task List

#### Description
Extend the page with a function named `loadTasks()` that fetches task data from a REST API and renders each task in a list.

#### Requirements
Completed program should:

- Send a GET request to `/api/tasks`
- Parse the JSON response and create a list of tasks in the page content
- Display each task title and description
- Show a message when no tasks are returned

### 🛠️ Task 3: Submit a New Task

#### Description
Add a form that lets users create a new task. When the form is submitted, send a POST request and display the response.

#### Requirements
Completed program should:

- Add a form with inputs for task title and description
- Send a POST request to `/api/tasks` with JSON body data
- Display the response from the API, including any generated task ID
- Handle validation errors and display a helpful message if the request fails

## 💡 Notes

- Run your FastAPI application locally on `http://localhost:8000`
- If you are using CORS, confirm your FastAPI backend allows requests from your static page origin
- Test the page in a browser and open the developer console to inspect request responses
