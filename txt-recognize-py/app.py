import time

from text_recognizer import get_clipboard_image, text_from_clipboard_image, get_all_images_names
from text_recognizer import image_text_from_image_folder

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


@app.route("/local_files_recognition")
def local_files_recognition():
	img_names = get_all_images_names()
	text = image_text_from_image_folder(img_names)
	print(text)
	return jsonify({ "text": text })


if __name__ == "__main__":




	app.run(debug=True)