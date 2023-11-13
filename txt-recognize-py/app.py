import time

from text_recognizer import get_all_images_names, get_clipboard_image, text_from_clipboard_image
from text_recognizer import execution_end_sound, image_text_from_image_folder

from flask import Flask, render_template

app = Flask(__name__, static_folder="assets")

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
	# start_time = time.time()
	
	# clipboard_image = get_clipboard_image()
	# if clipboard_image:
	# 	text_from_clipboard_image(clipboard_image)
	# 	execution_end_sound()

	# img_names = get_all_images_names()
	# text = image_text_from_image_folder(img_names)

	# end_time = time.time()
	# total_time = end_time - start_time
	# print(f"Character recognition completed in {round(total_time)} seconds")

	# if text:
	# 	with open("output_file.txt", "w", encoding="utf-8") as file:
	# 		file.write(text)
	# 	print("Recognized text saved in output_file.txt")

    app.run(debug=True)