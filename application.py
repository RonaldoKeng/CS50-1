import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Goodreads API
import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "xhkXxRzctHjfRU0tqg", "isbns": "9781632168146"})
print(res.json())

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    """BeeBook's Homepage"""

    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    """Logins an existing user"""

    # Clear existing login
    session.clear()

    # If form submitted
    if request.method == "POST":
        return render_template("login.html")
        # Finds user
        
        # Confirms correct password

        # Remember session ID

        # Redirect to homepage
    
    # If directed to /login
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Logs user out"""

    # Clear existing login
    session.clear()

    # Redirect to homepage
    return render_template("index.html")

@app.route("/register")
def register():
    """Registers a new user"""

    # Clear existing login
    session.clear()

    # If form submitted
    if request.method == "POST":

        # Store inputs in variables

        # Check all inputs have been filled

        # Check password matches

        # Hash the password

        # Insert user into database

        # Store user in session
        return render_template("register.html")
    
    # If directed to /register
    else:
        return render_template("register.html")