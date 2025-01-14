# FastAPI TodoApp

## Overview
FastAPI TodoApp is a full-stack task management application built with FastAPI. It features seamless database integration, modular API route management, dynamic template rendering, and comprehensive unit testing to ensure reliability and maintainability.

## Features
- **RESTful API**: Implements CRUD operations for task management.
- **Database Integration**: Utilizes SQLAlchemy and Alembic for schema management and migrations.
- **Template Rendering**: Dynamically generates HTML pages using Jinja2.
- **Unit Testing**: Ensures reliability with pytest for validating API endpoints.

## Technologies Used
- **Backend**: FastAPI
- **Database**: SQLAlchemy with SQLite
- **Migrations**: Alembic
- **Frontend**: Jinja2 for templates
- **Testing**: pytest

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TodoApp
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   alembic upgrade head
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure
```
TodoApp/
├── main.py            # Entry point of the application
├── database.py        # Database connection setup
├── models.py          # SQLAlchemy models
├── routers/           # Modular API route definitions
├── templates/         # HTML templates
├── static/            # Static files (CSS, JavaScript)
├── alembic/           # Database migration scripts
├── tests/             # Unit tests
└── requirements.txt   # Project dependencies
```

## API Endpoints
| Method | Endpoint       | Description                 |
|--------|----------------|-----------------------------|
| GET    | `/tasks`       | Retrieve all tasks          |
| GET    | `/tasks/{id}`  | Retrieve a task by ID       |
| POST   | `/tasks`       | Create a new task           |
| PUT    | `/tasks/{id}`  | Update an existing task     |
| DELETE | `/tasks/{id}`  | Delete a task               |

## Testing
Run unit tests using pytest:
```bash
pytest
```

## Future Enhancements
- Add user authentication and authorization.
- Implement advanced task filtering and sorting options.
- Deploy the application to a cloud service like AWS or Azure.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the FastAPI and SQLAlchemy communities for their excellent documentation and support.
