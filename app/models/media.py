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
                  "id": self.id,
                  "isMovie": self.is_movie,
                  "TMDB_id": self.TMDB_id,
                  "title": self.title,
            }
            return media_dict

      def get_media_reviews_json(self):
            if not self.reviews:
                  return None

            json_reviews = []
            for review in self.reviews:
                  json_reviews.append(review.to_json())

            return json_reviews

      @classmethod
      def from_json(cls, json_response):
            media = Media(TMDB_id= json_response["TMDB_id"],
                        is_movie=json_response["isMovie"],
                        title=json_response["title"])

            return media