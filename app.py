# ------------ app.py ------------
from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    meme_files = os.listdir('static/memes')
    selected_meme = random.choice(meme_files)
    return render_template('index.html', meme=selected_meme)

@app.route('/start_timer')
def start_timer():
    return jsonify({"status": "Timer started!"})

if __name__ == '__main__':
    app.run(debug=True)
