from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
@bp_main.route('/<name>/')
def index(name=’World’):
    return render_template('index.html', name=name)
