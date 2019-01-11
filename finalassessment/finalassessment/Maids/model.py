from finalassessment import db


class Maids(db.Model):

    __tablename__ = 'maids'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    age = db.Column(db.String(), nullable=False)
    image = db.Column(db.Text)
    price=db.Column(db.Numeric())
    description= db.Column(db.String())
    orders = db.relationship("Orders", backref="maids", lazy=False,
                            cascade="delete, delete-orphan")
    

    def __init__(self, name, country, age, price, description=None):
        self.name = name
        self.country = country
        self.age = age
        self.image = price
        self.description = description
