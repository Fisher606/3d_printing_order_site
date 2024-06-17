from flask import render_template, flash, redirect, url_for, request
from app import db
from app.forms import LoginForm, RegistrationForm, OrderForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Order
from werkzeug.urls import url_parse
from app import create_app

app = create_app()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
