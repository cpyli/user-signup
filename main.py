from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config["DEBUG"] = True
  
user_signup = """
    <style>
        .error {{ color: red; }}
    </style>

    <h1>User Signup</h1>

    <form method="POST">
        <label>Username:
            <input name="username" type="text" value="{username}" />
        </label>
        <p class="error">{username_error}</p>

        <label>Password:
            <input name="password" type="password" value="{password}" />
        </label>
        <p class="error">{password_error}</p>

        <label>Verify Password:
            <input name="verify_password" type="password" value="{verify_password}" />
        </label>
        <p class="error">{verify_password_error}</p>

        <label>E-mail (Optional):
            <input name="email" type="text" value="{email}" />
        </label>
        <p class="error">{email_error}</p>

        <input type="submit" />

    </form>
    """

@app.route("/")
def display_user_signup():
    return user_signup.format(username="", password="",
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
        password_error = "Not a valid password"
        password = ""
    else:
        password = password

    if not is_username_password_valid(verify_password):   
        verify_password_error = "Not a valid password"
        verify_password = ""
    else:
        verify_password = verify_password

    if password != verify_password:        
        password_error = "Passwords did not match"        
        verify_password_error = "Passwords did not match"
        password = ""
        verify_password = ""

    if not is_email_valid(email):   
        email_error = "Not a valid e-mail"
        email = email
    else:
        email = email

    if not username_error and not password_error:
        username = username
        return redirect("/welcome?username={0}".format(username))
    else:
        return user_signup.format(username=username, password="",
        verify_password="", email=email,
        username_error=username_error, password_error=password_error,
        verify_password_error=verify_password_error, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return "<h1>Welcome, {0}!</h1>".format(username)

app.run()