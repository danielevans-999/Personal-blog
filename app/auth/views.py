from flask import render_template,request,redirect,url_for,flash
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db


@auth.route('/register' , methods=["GET","POST"])
def register ():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data,username=username.data)
    
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
        flash('Registered successfully !')
    title = "New Account"
    return render_template('auth/register.html',title=title,registration_form = form)