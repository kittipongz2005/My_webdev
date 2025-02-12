from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddTeamForm(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Add Team')

class AddPlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    team_id = IntegerField('Team ID', validators=[DataRequired()])
    submit = SubmitField('Add Player')
