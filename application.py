from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', env = os.environ['ENVIRONMENT'])
    
if __name__ == "__main__":
    app.run(debug=True, port=5000, host = '0.0.0.0')