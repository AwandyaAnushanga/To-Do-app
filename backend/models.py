from config import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=True, nullable=False)
   

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
        }
