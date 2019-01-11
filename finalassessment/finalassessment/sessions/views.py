from finalassessment.users.model import User, db
from finalassessment.sessions.forms import LogInForm
from flask_login import login_user, current_user, login_required, logout_user
from flask import redirect, url_for, render_template, Blueprint, flash, request
# from bidboard import oauth, google, GOOGLE_REDIRECT_URI
# from bidboard.helpers.sendgrid import send_signup_email
import random

sessions_blueprint = Blueprint(
    'sessions', __name__, template_folder='templates')


@sessions_blueprint.route('/login', methods=['GET'])
def new():
    if current_user.is_authenticated:
        flash('You\'re already logged in!')
        return redirect(url_for('home'))  # change redirect destination later
    else:
        form = LogInForm()
        return render_template('sessions/sign_in.html', form=form)


@sessions_blueprint.route("/login", methods=['POST'])
def authenticate():
    form = LogInForm()
    user = User.query.filter_by(email=form.email.data.lower()).first()

    if user and user.check_password(form.password.data):
        login_user(user, remember=False)
        flash('Logged in successfully')
        next = request.args.get('next')
        # change redirect destination later
        return redirect(next or url_for('home', id=current_user.id))

    else:
        flash('Wrong Email/Password')
        return render_template('sessions/sign_in.html', form=form)


@sessions_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('home'))





