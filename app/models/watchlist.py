from app import db
from .user import User 
from .media import Media

class Watchlist(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      watched = db.Column(db.Boolean, default=False, nullable=False)
      user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
      user = db.relationship("User", back_populates="watchlist")
      media_id = db.Column(db.Integer,db.ForeignKey("media.id"))
      media = db.relationship("Media", back_populates="watchlists")
      
      def to_json(self):
            entry = {
                  "id": self.id,
                  "watched": self.watched,
                  "user": self.user.get_id_username_dict()
                  #"media": self.media.get_search_result_dict()
            }
            return entry


