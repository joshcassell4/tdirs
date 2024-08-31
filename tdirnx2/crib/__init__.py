from flask import Flask
import os
import importlib
from flask import render_template
#print(__name__)
#runmod = __import__(__name__)
from . import blueprints
from .blueprints.things import THINGS


app = Flask(__name__)
def defhome():
    #return render_template('home.html', things=THINGS)
    return render_template('home2.html', things=THINGS)

app.add_url_rule(rule=f"/testit",
                        view_func=defhome,
                     methods=["GET"])
#first=False
for bp in blueprints.bps:
    #print(bp)
    #if not first:
    app.register_blueprint(bp[1],url_prefix='/' + str(bp[0]))
    #else:
    #    print(bp[1],bp[0])
    #   app.register_blueprint(bp[1],url_prefix='/' + str(bp[0]))