from . import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False) 

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"<Player {self.name}>"

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    team_a_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team_b_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)