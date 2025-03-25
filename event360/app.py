import os
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_migrate import Migrate

# Flask App Initialization
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'your_secret_key'

app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event360.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
# -------------------------
# 📚 DATABASE MODELS
# -------------------------

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Event Model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(50), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    fee = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)  # ✅ Add image field

# Admin Credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

# -------------------------
# 📍 ROUTES
# -------------------------

# Home Route (Display Events for Users)
@app.route('/')
def home():
    events = Event.query.all()
    return render_template('index.html', events=events)

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            return redirect(url_for('demo'))  # ✅ Redirect to Event Page
        else:
            return "Invalid Credentials. Please try again."

    return render_template('login.html')

# User Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['signup-name']
        email = request.form['signup-email']
        password = request.form['signup-password']

        # Check if email already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('signup.html', error="Email already registered. Please log in.")

        # Hash password before storing
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

# Demo Page (After User Login to Register for Events)
@app.route('/demo', methods=['GET'])
def demo():
    if 'user_id' in session:
        events = Event.query.all()
        return render_template('demo.html', name=session['user_name'], events=events)

    return redirect(url_for('login'))

# User Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('admin_logged_in', None)
    return redirect(url_for('home'))

# -------------------------
# 🔐 ADMIN ROUTES
# -------------------------

# Admin Login Route
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid Admin Credentials. Try Again!"
    return render_template('admin_login.html')

# Admin Dashboard - Manage Events
@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    events = Event.query.all()
    return render_template('admin_dashboard.html', events=events)

# Add New Event (Admin Only) with Image Upload
@app.route('/add-event', methods=['POST'])
def add_event():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    title = request.form['title']
    event_date = request.form['event_date']
    event_type = request.form['event_type']
    fee = request.form['fee']
    link = request.form['link']

    # Handling Image Upload
    image_file = request.files['image']
    if image_file and image_file.filename != '':
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(image_path)
        image_url = f'static/uploads/{filename}'
    else:
        image_url = 'static/uploads/default.jpg'  # Default image

    # Save event to DB
    new_event = Event(title=title, event_date=event_date, event_type=event_type, fee=fee, link=link, image=image_url)
    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for('admin_dashboard'))
# File Type Validation for Images
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Delete Event (Admin Only)
@app.route('/delete-event/<int:event_id>', methods=['GET'])
def delete_event(event_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))


# -------------------------
# 🔥 DATABASE INITIALIZATION
# -------------------------
with app.app_context():
    db.create_all()

# -------------------------
# 🚀 RUN THE APPLICATION
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
