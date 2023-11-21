import time

from text_recognizer import get_clipboard_image, text_from_clipboard_image

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="assets")

@app.route("/")
def hello_world():
	return render_template("index.html")

@app.route("/clipboard_recognition")
def clipboard_recognition():
	clipboard_image = get_clipboard_image()

	if clipboard_image:
		text = text_from_clipboard_image(clipboard_image)
		return jsonify({ "text": text })
	
	return jsonify({ "text": "" })


if __name__ == "__main__":
	app.run(debug=True)