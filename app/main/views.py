from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website '
    return render_template('index.html',title = title)


@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    '''
    View pitch page function that returns pitch details and data 
    '''