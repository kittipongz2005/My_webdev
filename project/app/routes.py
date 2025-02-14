from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Team
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/teams')
def teams():
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@main_bp.route('/add_team', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']

        if not name or not city:
            flash("Both fields are required!", "danger")
        else:
            new_team = Team(name=name, city=city)
            db.session.add(new_team)
            db.session.commit()
            flash("Team added successfully!", "success")
            return redirect(url_for('main.teams'))

    return render_template('add_team.html')

@main_bp.route('/edit_team/<int:team_id>', methods=['GET', 'POST'])
def edit_team(team_id):
    team = Team.query.get_or_404(team_id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.city = request.form['city']
        db.session.commit()
        flash("Team updated successfully!", "success")
        return redirect(url_for('main.teams'))
    return render_template('edit_team.html', team=team)

@main_bp.route('/delete_team/<int:team_id>', methods=['POST'])
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    flash("Team deleted successfully!", "success")
    return redirect(url_for('main.teams'))
