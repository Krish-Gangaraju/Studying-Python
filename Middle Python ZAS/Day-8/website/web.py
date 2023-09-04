from flask import Flask, render_template, request


#### initialize the flask app.

app = Flask(__name__)

################################
# home page
################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('index.html')
	
################################
# contact page routing
################################


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
	
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
	
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)