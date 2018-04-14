# Import flask dependencies
from flask import Blueprint, request, render_template
from backend import app


@app.route('/', defaults={'path': ''})
def index(path):
    """Render landing page."""
    # return render_template('index.html', title="index")
    return app.send_static_file("index.html")


@app.route('/play')
def play():
    """Render play page, for playing bpmninja."""
    return render_template('play.html', title="play")
