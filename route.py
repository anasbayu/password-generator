from flask import Flask
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return '<img src="https://devstatic-tokodaring.tisera.id/dev/images/produk_gambar/pb.jpg" alt="img"/>'


@app.route('/api', methods=['GET'])
def api():
    return generator.generate()