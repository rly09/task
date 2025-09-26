from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List
import json
import os

app = FastAPI()

# Enable CORS so Flutter can call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON file to store registrations
DATA_FILE = "registrations.json"

# Load existing registrations if file exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            registrations = json.load(f)
        except json.JSONDecodeError:
            registrations = []
else:
    registrations = []

# Pydantic model for input validation
class Registration(BaseModel):
    name: str
    email: EmailStr

# Save registrations to JSON
def save_registrations():
    with open(DATA_FILE, "w") as f:
        json.dump(registrations, f, indent=4)

@app.post("/register")
def register_user(reg: Registration):
    # Prevent duplicate emails
    for r in registrations:
        if r["email"] == reg.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    registrations.append({"name": reg.name, "email": reg.email})
    save_registrations()
    print("New registration:", reg.dict())
    return {"message": "Registration successful", "data": reg.dict()}

@app.get("/registrations")
def get_registrations() -> List[dict]:
    return registrations
