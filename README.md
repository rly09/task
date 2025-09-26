# Club Event Registration App

A **Flutter + FastAPI** event registration application for college clubs.  
This app allows users to register for events, and admins or organizers can view all registrations.  

The project is split into:

- **Frontend**: Flutter mobile app  
- **Backend**: FastAPI server with JSON-based storage  

---

## Features

### Frontend (Flutter)

- Minimal & modern **glassmorphic UI**  
- Registration form with validation:  
  - Name (required)  
  - Email (required, valid email format)  
- Success & error messages for registration  
- **View Registrations** page with pull-to-refresh  
- Smooth scrolling and responsive design  
- Custom fonts using **Google Fonts**

### Backend (FastAPI)

- REST API endpoints:  
  - `POST /register` → Add a new registration  
  - `GET /registrations` → Retrieve all registrations  
- Stores registrations in a **JSON file** (`registrations.json`)  
- Validates email uniqueness to prevent duplicates  
- CORS enabled for cross-origin requests from Flutter  

---


