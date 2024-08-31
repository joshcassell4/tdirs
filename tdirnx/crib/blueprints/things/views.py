from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint

#from my_app.product.models import THINGS
from .models import THINGS

blueprint = Blueprint('things', __name__)
@blueprint.route('/')
@blueprint.route('/home')
def home():
    #return render_template('home.html', things=THINGS)
    return render_template('home2.html', things=THINGS)
@blueprint.route('/things/<key>')
def thing(key):
    thing = THINGS.get(key)
    if not thing:
        abort(404)
    return render_template('thing.html', thing=thing)
@blueprint.context_processor
def some_processor():
    def name_uuid(thing):
        return '{0} / {1}'.format(thing.name, thing.uuid)
    return {'full_name': 'full_name'}