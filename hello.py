from flask import Flask
from flask import send_file
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return 'Placechicks!'

@app.route("/<int:width>/<int:height>")
def getChicks(width,height):
	random = randint(0,20)
	image = 'chicks/' + str(random) + '.jpg'
	return send_file(image, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run()