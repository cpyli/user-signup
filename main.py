from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def display_user_signup():
    template = jinja_env.get_template("index.html")
    return template.render(username="", password="",
    verify_password="", email="",
    username_error="", password_error="",
    verify_password_error="", email_error="")

def is_username_password_valid(user_input):
    if len(user_input) > 2 and len(user_input) < 21:
        if " " not in user_input:
            return True
    else:
        return False
        
def is_email_valid(user_input):
    if len(user_input) > 2 and len(user_input) < 21:
        if " " not in user_input:
            if "@" in user_input and "." in user_input:
                return True
    elif user_input == "":
        return True
    else:
        return False

@app.route("/", methods=["POST"])
def signup_error():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if not is_username_password_valid(username):
        username_error = "Not a valid username"
        username = username
    else:
        username = username

    if not is_username_password_valid(password):   
        password_error = "Not a valid password. Must be 3 to 20 characters long and contain no spaces."
        password = ""
    else:
        password = password

    if not is_username_password_valid(verify_password):   
        verify_password_error = "Not a valid password. Must be 3 to 20 characters long and contain no spaces."
        verify_password = ""
    else:
        verify_password = verify_password

    if not password_error and not verify_password_error:
        if password != verify_password:        
            password_error = "Passwords did not match. Must be 3 to 20 characters long and contain no spaces."        
            verify_password_error = "Passwords did not match. Must be 3 to 20 characters long and contain no spaces."
            password = ""
            verify_password = ""

    if not is_email_valid(email):   
        email_error = "Not a valid e-mail. Must be 3 to 20 characters long and contain no spaces."
        email = email
    else:
        email = email

    if not username_error and not password_error and not email_error:
        username = username
        return redirect("/welcome?username={0}".format(username))
    else:
        template = jinja_env.get_template("index.html")
        return template.render(username=username, password="",
        verify_password="", email=email,
        username_error=username_error, password_error=password_error,
        verify_password_error=verify_password_error, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    template = jinja_env.get_template("welcome.html")
    return template.render(username=username)

app.run()