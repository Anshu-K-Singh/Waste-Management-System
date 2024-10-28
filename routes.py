from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask import Blueprint
from forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
   
    return render_template("index.html")

@main.route('/register', methods=['GET', 'POST'])
def register():
    """
    This route handles user registration.
    It displays a registration form (GET request) and processes the submitted data (POST request).
    If the form is valid, it creates a new User object, saves it to the database, and redirects the user to the login page.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )
        #user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
  
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Compare plain-text passwords
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.user_dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route('/user_dashboard')
def user_dashboard():
   
    return "Welcome to your User Dashboard!"

def register_routes(app):
    """
    This function registers the 'main' Blueprint with the Flask app.
    This tells Flask to use the routes defined in the 'main' Blueprint when handling requests.
    """
    app.register_blueprint(main)
