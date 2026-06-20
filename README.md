# Internship / Job Application Tracker API

A personal REST API built with Django and Django REST Framework to help track internship and job applications.

This project allows users to:

- Track companies they have applied to
- Manage job applications
- Record interview details
- Store recruiter and employee contacts
- Monitor application progress through different stages
- Keep all internship/job search information organized in one place

---

## Features

### Authentication
- Token Authentication
- User Registration
- User Login
- User-specific data access

### Company Management
- Create companies
- View companies
- Update company information
- Delete companies

### Application Tracking
- Record job applications
- Track application status
- Add notes
- View application history

### Interview Management
- Schedule interviews
- Record interview rounds
- Store interview feedback

### Contact Management
- Save recruiter information
- Save employee contacts
- Store emails and LinkedIn profiles

### API Features
- RESTful API
- CRUD Operations
- Pagination
- Filtering
- Search
- Nested Serializers

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Token Authentication

---

## Database Structure

### Company

Represents a company where applications are submitted.

Fields:

- name
- website
- location
- created_at

### Application

Represents a job or internship application.

Fields:

- company
- position
- status
- date_applied
- notes

### Interview

Represents interview rounds for an application.

Fields:

- application
- interview_date
- round_name
- feedback

### Contact

Represents company contacts.

Fields:

- company
- name
- role
- email
- linkedin

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /api/register/ | Register user |
| POST | /api/login/ | Login user |
| POST | /api/logout/ | Logout user |

---

### Companies

| Method | Endpoint |
|----------|----------|
| GET | /api/companies/ |
| POST | /api/companies/ |
| GET | /api/companies/{id}/ |
| PUT | /api/companies/{id}/ |
| DELETE | /api/companies/{id}/ |

---

### Applications

| Method | Endpoint |
|----------|----------|
| GET | /api/applications/ |
| POST | /api/applications/ |
| GET | /api/applications/{id}/ |
| PUT | /api/applications/{id}/ |
| DELETE | /api/applications/{id}/ |

---

### Interviews

| Method | Endpoint |
|----------|----------|
| GET | /api/interviews/ |
| POST | /api/interviews/ |
| GET | /api/interviews/{id}/ |
| PUT | /api/interviews/{id}/ |
| DELETE | /api/interviews/{id}/ |

---

### Contacts

| Method | Endpoint |
|----------|----------|
| GET | /api/contacts/ |
| POST | /api/contacts/ |
| GET | /api/contacts/{id}/ |
| PUT | /api/contacts/{id}/ |
| DELETE | /api/contacts/{id}/ |

---

## Future Improvements

- JWT Authentication
- Dashboard Analytics Endpoint
- Upcoming Interview Endpoint
- Resume Storage
- Application Deadline Tracking
- Email Notifications
- PostgreSQL Support
- Docker Deployment

---

## Learning Objectives

This project was built to practice:

- Django Models
- Model Relationships
- Django REST Framework
- Serializers
- Nested Serializers
- ViewSets
- Routers
- Authentication
- Permissions
- Pagination
- Filtering
- API Design

---

## Author

Built as a learning project to strengthen Django REST Framework skills and API development concepts.