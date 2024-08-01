#!/usr/bin/python3
"""
The module contains a script that starts a web application
Fetches data from the storage engine
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    """Removes the current SQLAlchemy Session"""
    from models import storage

    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a html page inside the 'BODY' tag"""
    from models import storage as db
    from models.state import State

    states = db.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
