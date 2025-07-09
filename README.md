
# 🎓 Django REST API – Student Course Enrollment System (with JWT Authentication)

This project is a **Django REST API** that manages a student course enrollment system with secure **JWT-based authentication**. It allows registered users to manage students, teachers, courses, and course enrollments via RESTful endpoints.

---

## 🚀 Objective

Build a secure and scalable RESTful API using:

- Django & Django REST Framework (DRF)
- JWT authentication via `djangorestframework-simplejwt`

---
## 🧩 Apps Structure

- `students/`: Handles student-related logic.
- `teachers/`: Manages teacher data.
- `courses/`: Contains course models and views.
- `enrollments/`: Manages student-course enrollments.
- `employees/`: *(if used)* Handles user-related logic or admin features.

---

## 🧪 Testing the API

You can test the API using tools like:

- [Postman](https://www.postman.com/)

POST /api/token/

{

"username": "your_username",

"password": "your_password"

}

### 🔐 Authentication Required

- Before accessing any protected endpoint, **login** via:


---

## 🔐 Authentication (JWT)

Authentication is handled using **JSON Web Tokens (JWT)** with the `djangorestframework-simplejwt` package.

### 📌 Token Endpoints:

| Action | Endpoint        | Method | Description                         |
|--------|------------------|--------|-------------------------------------|
| Login  | `/api/token/`    | POST   | Obtain access and refresh tokens    |


All other API routes **require** a valid JWT access token in the header:

```http
Authorization: Bearer <access_token>
