from flask import Flask, render_template
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def api():
    return generator.generate()