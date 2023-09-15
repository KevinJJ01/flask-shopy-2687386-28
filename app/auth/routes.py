from flask_login import login_user, current_user, logout_user
from flask import render_template,redirect,flash
from flask_login import login_required
from app.auth import auth 
from .forms import LoginForm
import app

@auth.route('/login',
            methods = ['GET', 'POST'])
@login_required
def login():
    form= LoginForm()
    if form.validate_on_submit():
        #selection the user for username
        c = app.models.Cliente.query.filter_by(username = form.username.data).first()
        if c is None or not c.check_password(form.password.data): 
            flash ('user dont exist or password invalidate')
            return redirect('/auth/login')
        #message flask the user not existed 
        else: 
            login_user(c, remember= True)
            return redirect('/productos/listar')
    return render_template("login.html",
                           form=form)

@auth.route('logout',  )
def logout():
    logout_user()
    flash("logout exite confirmed")
    return redirect('/auth/login')