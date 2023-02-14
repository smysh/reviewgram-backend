from app import db
import datetime as dt
from .user import User
from .media import Media

class Review(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
      user = db.relationship("User", back_populates="reviews")
      rating = db.Column(db.Float)
      content = db.Column(db.Text,nullable=False )
      date_created = db.Column(db.DateTime, default=dt.datetime.now())
      date_updated = db.Column(db.DateTime, default=dt.datetime.now())
      media_id = db.Column(db.Integer, db.ForeignKey("media.id"))
      media = db.relationship("Media", back_populates="reviews")