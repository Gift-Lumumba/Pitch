from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website '
    return render_template('index.html',title = title)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
  '''
  View pitch page function that returns the pitch details and its data
  '''

  return render_template('pitch.html',id = pitch_id)