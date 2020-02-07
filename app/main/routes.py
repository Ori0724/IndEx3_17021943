from flask import render_template, Blueprint, flash, redirect, url_for, request

from app.main.forms import SignupForm

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
@bp_main.route('/<name>/')
def index(name="World"):
    return render_template('index.html', name=name)


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Signup requested for {}'.format(form.name.data))
        return redirect(url_for('main.index'))
    return render_template('signup.html', form=form)
