# FastAPI Social Media API

This project implements a social media API using FastAPI, a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

* **User Authentication:** Secure user registration and login using OAuth2.
* **Post Management:** Create, read, update, and delete posts.
* **Voting System:** Users can upvote or downvote posts.
* **Database Interaction:** Uses SQLAlchemy for database operations.
* **Testing:** Includes unit tests for core functionalities.


## Technologies Used

* **FastAPI:** Web framework
* **Python:** Programming language
* **SQLAlchemy:** Database ORM
* **PostgreSQL:** Database (or MySQL, configurable)
* **OAuth2:** Authentication


## Getting Started

1. **Clone the repository:**
```
bash
git clone <repository_url>
```
2. **Install dependencies:**
```
bash
pip install -r requirements.txt
```
3. **Configure the database:**

   * Create a PostgreSQL database (or MySQL).
   * Update the database connection settings in `app/config.py`.


4. **Run the application:**
```
bash
uvicorn app.main:app --reload
```
5. **Run tests**
```
bash
pytest
```
## Project Structure
```
.
├── Dockerfile             # Docker configuration
├── alembic.ini            # Alembic configuration
├── docker-compose.yml      # Docker Compose configuration
├── get-pip.py             # Helper script
├── gunicorn.service       # Gunicorn service file
├── requirements.txt       # Project dependencies
├── test                   # Test files
├── .idx                   # Nix configuration
├── .vscode                # VS Code configuration
├── alembic                # Alembic migration files
│   └── ...
├── app                    # Application code
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   ├── utils.py
│   ├── routers             # API routes
│   │   └── ...
│   └── ...
└── tests                 # Test suite
    └── ...
```
## API Endpoints

Refer to the individual route files (`app/routers/*.py`) for details on each API endpoint.


## Contributing

Contributions are welcome! Feel free to submit pull requests.


## License

[Specify license here]