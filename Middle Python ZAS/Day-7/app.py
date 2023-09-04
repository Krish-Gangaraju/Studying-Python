from flask import Flask, render_template, request

#### initialize the flask app.

app = Flask(__name__)

################################
# home page
################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	return '<h1>Welcome to my website</h1>'