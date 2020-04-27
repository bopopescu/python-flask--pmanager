from datetime import timedelta
from flask import session, request, redirect, url_for
from pmanager import app
from functools import wraps

def is_logged():
    num = 1
    # if session.get('authenticated_user'):
    if num == 1:
        return True
        # if session['authenticated_user'] is not None:
        #     return True
    else:
        return redirect('home')

is_logged = is_logged()


class Auth:

    # this construct will first check if the log in session is already set
    # if the login session is set then it sets some properties
    def __init__(self):
        pass

    def log_user(self, user="", rememberMe=False):
        session.permanent = True
        session["auth_id"] = user["id"]
        session["auth_name"] = user["name"]
        session["logged_in"] = True
        session["authenticated_user"] = user

        if rememberMe == False:
            app.permanent_session_lifetime = timedelta(minutes=120)


        return self

    def logout(self):
        session.clear()

        return self

    # create a function that returns the data of the current user (id or email)
    def get_id(self):
        pass

    def get_email(self):
        pass

    def is_admin(self):
        pass

    def is_anonymous(self):
        pass

    def remember(self):
        pass

def is_logged(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

login_required = is_logged
