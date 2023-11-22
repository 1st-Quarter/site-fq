#import statements
from flask import Flask, render_template, url_for, request, redirect

# Flask app
app = Flask(__name__)

# Pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contribute/')
def contribute():
    return render_template('contribute.html')

@app.route('/partners/')
def partners():
    return render_template('partners.html')

@app.route('/initiatives/')
def initiatives():
    return render_template('initiatives.html')

if __name__ == "__main__":
    app.run(debug=True)