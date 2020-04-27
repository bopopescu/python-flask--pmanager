from flask import render_template, redirect, url_for, request, redirect, flash, session
from pmanager import app, bcrypt
from database import Database
from pmanager.forms import TaskForm, RegistrationForm, LoginForm
from auth import Auth, login_required
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

db_query = Database()
authenticate = Auth()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks")
def tasks():

    tasks = db_query.all("tasks")
    return render_template("tasks.html", tasks=tasks)


@app.route("/task/<int:task_id>", methods=['GET', 'POST'])
def task_edit(task_id):

    task = db_query.select_where("tasks", "id", task_id)

    if request.method == 'POST':

        db_query.update_where("tasks", "id", task_id, request.form)
        # flash("Task {} successfully updated", 'green').fornat(task_id)

        return redirect(url_for('tasks'))


    return render_template('task_edit.html', task=task)


@app.route("/task/new", methods=['GET','POST'])
def task_new():

    form = TaskForm()

    if request.method == 'POST':

        db_query.insert("tasks", request.form)
        flash("Task successfully added", "green")
        return redirect(url_for('tasks'))


    return render_template("task_new.html", form=form)

@app.route("/task/<int:task_id>/delete")
def task_delete(task_id):

    db_query.delete_where("tasks", "id", task_id)
    return redirect(url_for('tasks'))

##################### AUTHENTICATION ####################

@app.route("/login", methods=['GET', 'POST'])
def login():

    if session.get('authenticated_user'):
        if session['authenticated_user'] is not None:
            return redirect(url_for('home'))

    form = LoginForm()
    if request.method == "GET":
        return render_template('login.html', form=form)
    else:
        user = db_query.select_where("users", "name", form.name.data)

        if user and bcrypt.check_password_hash(user['password'], form.password.data):

            authenticate.log_user(user)
            return redirect(url_for('home'))

        else:
            flash("Authentication failed", 'error')
            return redirect(url_for('login'))


@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if request.method == 'GET':
        return render_template('register.html', title='Register', form=form)

    else:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

            data = {
                "name": form.name.data,
                "email": form.email.data,
                "password": hashed_password,
            }

            db_query.register_user("users", data)

            flash('Account created! You may now login', 'success')
            return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    authenticate.logout()

    return redirect(url_for('home'))