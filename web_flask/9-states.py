#!/usr/bin/python3
"""A script that imports Flask to run web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def teardown(self):
    """Removes current SQLALCHEMY session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def state():
    """Returns HTML page cotaining states"""
    states = storage.all("State")
    return render_template('9-states.html', states=states, mode=all)

@app.route('/state/<id>', strict_slashes=False)
def state_by_id(id):
    """Returns HTML page cotaining states"""
    for state in storage.all("State").values:
       return render_template('9-states.html', states=state, mode=id)
    return render_template('9-states.html', states=state, mode='none')
    




if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)