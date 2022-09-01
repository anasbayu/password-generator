from flask import Flask
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api', methods=['GET'])
def api():
    return generator.generate()