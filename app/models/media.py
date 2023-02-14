from app import db

class Media(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      is_movie = db.Column(db.Boolean, nullable=False)
      TMDB_id = db.Column(db.Integer, nullable=False)
      title = db.Column(db.String, nullable=False)
      reviews = db.relationship("Review", back_populates="media")
      watchlists= db.relationship("Watchlist", back_populates="media")

      def get_media_info_json(self):
            media_dict = {
                  "is_movie": self.is_movie,
                  "TMDB_id": self.TMDB_id,
                  "title": self.title,
            }
            return media_dict