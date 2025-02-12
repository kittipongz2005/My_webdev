from flask import Blueprint, render_template, redirect, url_for, request
from .models import Team, Player
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/teams")
def teams():
    teams = Team.query.all()
    return render_template("teams.html", teams=teams)

@main_bp.route("/players")
def players():
    players = Player.query.all()
    return render_template("players.html", players=players)
