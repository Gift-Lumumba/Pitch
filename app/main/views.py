from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile
from .. import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website'
    return render_template('index.html',title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


# # @main.route('/pitchs/new/',methods =['GET','POST'])
# # @login_required
# # def new_pitch():
# #     '''
# #     View new pitches posted

# #     '''


# @main.route('/comments/new/<int:pitch_id>',methods = ['GET','POST'])
# @login_required
# def new_comment(pitch_id):
#     '''
#     View new comments by users
#     '''


# @main.route('/pitchs/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
# @login_required
# def upvote(pitch_id):
#     '''
#     View pitch upvotes
#     '''


# @main.route('/pitchs/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
# @login_required
# def downvote(pitch_id):
#     '''
#     View pitch downvotes
#     '''
