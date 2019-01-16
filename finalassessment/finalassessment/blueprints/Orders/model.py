from finalassessment import db
from sqlalchemy.ext.hybrid import hybrid_property
import datetime


class Orders(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ordered_at = db.Column(db.Numeric(), nullable=False)
    amount = db.Column(db.Numeric(), db.ForeignKey('maids.price'), nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='MYR')


    def __init__(self, user_id, booking_at, amount):
        self.user_id = user_id
        self.booking_at = booking_at
        self.amount = amount

    @hybrid_property
    def ordered_at_readable(self):
        return datetime.datetime.fromtimestamp(self.created_at).strftime("%Y-%m-%d  %I:%M %p")

    
