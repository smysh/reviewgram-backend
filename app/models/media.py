from app import db

class Media(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      is_movie = db.Column(db.Boolean, nullable=False)
      TMDB_id = db.Column(db.Integer, nullable=False)
      title = db.Column(db.String(), nullable=False)
      review = db.relationship("Review", back_populates="media")
      watchlist= db.relationship("Watchlist", back_populates="media")