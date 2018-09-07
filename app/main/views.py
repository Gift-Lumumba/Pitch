from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website '
    return render_template('index.html',title = title)

