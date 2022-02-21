from db import db

class Feedback(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    img_path = db.Column("img_path",db.String(100), unique=False, nullable=False)
    mimetype = db.Column("mimetype",db.String(100), nullable=False)
    predict_class = db.Column("predict_class", db.String(10), nullable=True)
    actual_class = db.Column("actual_class",db.String(10), nullable=True)
    predict_right = db.Column("predict_right", db.String(5), nullable=True)

    def __init__(self, img_path, mimetype, predict_class=None ,predict_right=None, actual_class=None):
        self.img_path = img_path
        self.mimetype = mimetype
        self.predict_class = predict_class
        self.actual_class = actual_class
        self.predict_right = predict_right
