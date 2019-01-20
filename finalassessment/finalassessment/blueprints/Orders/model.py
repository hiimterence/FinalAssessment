from finalassessment import db
from sqlalchemy.ext.hybrid import hybrid_property
import datetime


class Orders(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ordered_at = db.Column(db.Numeric(), nullable=False)
    order_for_maid = db.Column(db.Integer, db.ForeignKey('maids.id'), nullable=False)

    def __init__(self, user_id, ordered_at,maid_id):
        self.user_id = user_id
        self.ordered_at = ordered_at
        self.maid_id = maid_id
     


    @hybrid_property
    def ordered_at_readable(self):
        return datetime.datetime.fromtimestamp(self.created_at).strftime("%Y-%m-%d  %I:%M %p")

    
