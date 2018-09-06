class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,author,comment):
        self.id =id
        self.author = author
        self.comment = comment

class Review:
  
    all_reviews = []

    def __init__(self,pitch_id,title,imageurl,review):
        self.pitch_id = pitch_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response