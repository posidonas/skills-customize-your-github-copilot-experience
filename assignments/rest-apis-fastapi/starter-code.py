"""
REST API with FastAPI - Starter Code

This is a template to help you get started building REST APIs with FastAPI.
Complete all three tasks by implementing the required endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Initialize the FastAPI application
app = FastAPI()

# Define request/response models using Pydantic
class Task(BaseModel):
    """Model for task data"""
    title: str
    description: Optional[str] = None

class User(BaseModel):
    """Model for user data"""
    user_id: int
    name: str
    email: str

# Task 1: Create a simple GET endpoint
# TODO: Implement the /api/greet endpoint
# The endpoint should return a JSON response with a greeting message and timestamp


# Task 2: Add dynamic endpoints with request parameters
# TODO: Implement GET /api/users/{user_id} endpoint
# TODO: Implement GET /api/search endpoint with query parameter 'q'


# Task 3: Implement POST endpoint with request body
# TODO: Implement POST /api/tasks endpoint
# TODO: Add error handling for invalid requests


if __name__ == "__main__":
    import uvicorn
    # Run the server with: uvicorn main:app --reload
    # OR use: python main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)
