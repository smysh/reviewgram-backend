from app import db

class User(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      name = db.Column(db.String(100), nullable=False)
      email = db.Column(db.String(100),nullable=False )
      user_name = db.Column(db.String(50), nullable=False)
      password = db.Column(db.String(50), nullable=False)
      watchlist = db.relationship("Watchlist", back_populates="user")
      reviews = db.relationship("Review", back_populates="user")

      def get_user_data_json(self):
            user_dict = {}
            user_dict["id"] = self.id
            user_dict["name"] = self.name
            user_dict["email"] = self.email
            user_dict["username"] = self.user_name

            return user_dict

      def get_id_username_dict(self):
            user_dict = {}
            user_dict["id"] = self.id
            user_dict["username"] = self.user_name

            return user_dict

      @classmethod
      def from_json(cls, json_obj):
            user = User(name=json_obj["name"],
                        email=json_obj["email"],
                        user_name=json_obj["username"],
                        password=json_obj["password"])

            return user


