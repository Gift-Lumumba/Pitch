from flask import render_template,request,redirect,url_for
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website '
    return render_template('index.html',title = title)

@app.route('/pitch/<int:id>')
def pitch(id):
  '''
  View pitch page function that returns the pitch details and its data
  '''

  return render_template('pitch.html',id = pitch_id)


@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)