
# Django Book Review Project

This is a Django-based project for managing book reviews. The project provides APIs for listing, creating, updating, and deleting books and reviews, as well as calculating book statistics.

## Features

- List and create books
- List and create reviews
- Retrieve, update, and delete individual books and reviews
- Calculate and return book statistics (average rating and review count)

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

## Setting Up the Project

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Apply the migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you want to access the Django admin site, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The project should now be running at `http://127.0.0.1:8000/`.

## API Endpoints

- **List and Create Books**: `GET /api/books/` | `POST /api/books/`
- **Retrieve, Update, and Delete a Book**: `GET /api/books/<id>/` | `PUT /api/books/<id>/` | `DELETE /api/books/<id>/`
- **List and Create Reviews**: `GET /api/reviews/` | `POST /api/reviews/`
- **Retrieve, Update, and Delete a Review**: `GET /api/reviews/<id>/` | `PUT /api/reviews/<id>/` | `DELETE /api/reviews/<id>/`
- **Book Statistics**: `GET /api/book-stats/`

## Notes

- **Database**: By default, the project uses SQLite as the database backend. If you're deploying the project or need a more robust database, consider configuring PostgreSQL or another database.

- **Environment Variables**: If you're using environment variables for sensitive data (e.g., secret keys, database credentials), make sure to set them up in your environment.

- **Static and Media Files**: Ensure proper configuration and storage for static and media files, especially when deploying.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
