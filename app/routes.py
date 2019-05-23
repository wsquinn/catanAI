from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('index'))
	return render_template('homepage.html', title='Welcome', form=form)

@app.route('/index', methods=['GET', 'POST'])
def index():
	
	return render_template('index.html')

