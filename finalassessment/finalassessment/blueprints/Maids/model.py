from finalassessment import db


class Maids(db.Model):

    __tablename__ = 'maids'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    age = db.Column(db.String(), nullable=False)
    image = db.Column(db.Text)
    scheduled_to_meet = db.Column(db.Text)
    place_to_meet = db.Column(db.Text)

    def __init__(self, name, country, age,image):
        self.name = name
        self.country = country
        self.age = age
        self.image = image