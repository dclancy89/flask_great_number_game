import random
from flask import Flask, render_template, request, redirect, session
from flask import Markup
app = Flask(__name__)
app.secret_key = "kfjieh838902fh30o2fhiosh0983w"

@app.route('/', methods=['GET', 'POST'])
def index():
	if session.get('num') is None:
		session['num'] = random.randrange(0,101)

	print session['num']

	res = ""
	c = ""
	button = ""

	if request.method == 'POST':
		display = ""
		guess = request.form['guess']
		print guess
		if int(guess) > session['num']:
			res = "Too High"
			c = "red"
		elif int(guess) < session['num']:
			res = "Too Low"
			c = "red"
		elif int(guess) == session['num']:
			res = str(session['num']) + " was the number!"
			c = "green"
			button = Markup('<a href="/restart" class="button">Play again!</a>')
			
	else:
		display = "hidden"

	return render_template('index.html', res=res, c=c, display=display, button=button)

@app.route('/restart')
def restart():
	session.pop('num')
	return redirect('/')

app.run(debug=True)