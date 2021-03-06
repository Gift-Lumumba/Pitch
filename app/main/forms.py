from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required,Email
from ..models import User,Pitch,Comment,Upvote,Downvote

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    category_id = SelectField('Select Category :', choices=[('Pickup Lines', 'Pickup Lines'),('Interview Pitch','Interview Pitch'),('Promotion Pitch','Promotion Pitch'),('Product Pitch','Product Pitch')])
    content = TextAreaField('Write your pitch here :')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment about the pitch:')
    submit = SubmitField('Add Comment')
