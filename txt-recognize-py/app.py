from tkinter import filedialog
import eel

from text_recognizer import (
	get_clipboard_image,
	text_from_clipboard_image,
	get_all_images_names,
	image_text_from_image_folder
)

eel.init("assets")

@eel.expose
def select_folder():
	selected_folder = filedialog.askdirectory()
	return selected_folder


@eel.expose
def clipboard_recognition(lang = "eng"):
	clipboard_image = get_clipboard_image()

	if clipboard_image:
		return text_from_clipboard_image(clipboard_image, lang)


@eel.expose
def local_files_recognition(lang = "eng"):
	img_names = get_all_images_names()
	return image_text_from_image_folder(img_names)


if __name__ == "__main__":
	eel.start("index.html")