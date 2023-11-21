#import statements
from flask import Flask, render_template, url_for, request, redirect

# Flask app
app = Flask(__name__)

# Pages
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)