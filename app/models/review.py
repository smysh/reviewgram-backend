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

      def to_json(self):
            review = {
                  "id": self.id,
                  "rating": self.rating,
                  "content": self.content,
                  "created": self.date_created.isoformat(),
                  "updated": self.date_updated.isoformat(),
                  "user": self.user.get_id_username_dict(),
                  "media": self.media.get_media_info_json(),
                  "fromTMDB": False
            }
            return review

      @classmethod
      def from_json(cls,json_response):
            review = Review(content=json_response["content"],
                        rating=json_response["rating"])
            return review

      def from_tmdb_json(cls,tmdb_response):
            review = Review(content=tmdb_response["content"],
                        rating=tmdb_response["author_details"]["rating"],
                        date_created=tmdb_response["created_at"],
                        date_updated=tmdb_response["updated_at"])

            return review