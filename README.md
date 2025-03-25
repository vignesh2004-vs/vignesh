# Event360

## Overview
Event360 is a web-based event management application built using Flask. It includes database models, static files, and templates to manage events efficiently. This application allows users to create, update, and manage event details seamlessly. The backend is powered by Flask with an SQLite database, while the frontend includes HTML, CSS, and JavaScript.

## Project Structure
```
event360/
│-- app.py                     # Main application entry point
│-- config.py                   # Configuration file
│-- event360.db                 # SQLite database file
│-- models.py                   # Database models
│-- instance/
│   └── event360.db             # Another instance of the database
│-- migrations/                 # Database migration files
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│       ├── c9e53c43bb51_added_image_column_to_event_table.py
│       ├── __pycache__/
│-- static/                     # Static assets (CSS, JS, Images)
│   ├── css/
│   │   ├── styles.css
│   ├── images/
│   │   ├── WhatsApp Image 2025-03-23 at 12.27.58_1df54e86.jpg
│   ├── js/
│   │   ├── chatbot.js
│-- templates/                  # HTML templates (not listed but expected)
```

## Features
- User-friendly interface to manage events
- Secure database storage using SQLite
- Responsive frontend using HTML, CSS, and JavaScript
- RESTful API endpoints for event management
- Database migration support with Alembic

## Setup and Installation
### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/event360.git
   cd event360
   ```
2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Setup Database Migrations**
   ```sh
   flask db upgrade
   ```
5. **Run the Application**
   ```sh
   python app.py
   ```
   The app should now be running at `http://127.0.0.1:5000/`

## Deployment
### Deploy on Railway (Recommended)
Railway provides a simple way to deploy Flask applications with database support.

1. **Push Code to GitHub**
2. **Create a New Railway Project** at [Railway](https://railway.app/)
3. **Deploy the Repository** by connecting your GitHub repo
4. **Set Environment Variables**
   - `DATABASE_URL` (for PostgreSQL or SQLite)
5. **Deploy and Get Live URL**

### Deploy on Render (Alternative)
Render offers free hosting for web applications with easy setup.

1. **Create an Account on [Render](https://render.com/)**
2. **Add New Web Service**
3. **Connect to GitHub Repository**
4. **Set Build and Start Commands**
   ```sh
   pip install -r requirements.txt
   python app.py
   ```
5. **Deploy and Get Live URL**

## Configuration
Modify `config.py` to set up database connections and other settings. Example settings:
```python
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///event360.db'
SECRET_KEY = 'your-secret-key'
```

## API Endpoints
| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/events`            | Fetch all events |
| POST   | `/events`            | Create a new event |
| GET    | `/events/<id>`       | Fetch a single event by ID |
| PUT    | `/events/<id>`       | Update an existing event |
| DELETE | `/events/<id>`       | Delete an event |

## License
This project is licensed under the MIT License.

## Contributing
If you wish to contribute, please fork the repository and submit a pull request with your changes. Bug reports and feature requests are welcome!

