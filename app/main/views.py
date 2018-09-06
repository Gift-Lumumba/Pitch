from flask import render_template,request,redirect,url_for
from . import main
from app.models import Review
from .forms import ReviewForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website '
    return render_template('index.html',title = title)

@main.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    title = f'{pitch.title}'
    reviews = Review.get_reviews(pitch.id)

    return render_template('pitch.html',title = title,pitch = pitch,reviews = reviews)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)