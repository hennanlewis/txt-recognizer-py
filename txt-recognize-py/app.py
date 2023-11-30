import tkinter as tk
from tkinter import filedialog
import eel
import os

from text_recognizer import (
	image_text_from_image_folder,
	text_from_clipboard_image,
	change_image_path_folder,
	get_all_images_names,
	get_clipboard_image
)

eel.init("assets")
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)


@eel.expose
def select_folder():
	selected_folder = filedialog.askdirectory()
	converted_path = os.path.abspath("images" if selected_folder == "" else selected_folder)
	
	change_image_path_folder(converted_path)


@eel.expose
def clipboard_recognition(lang = "eng"):
	clipboard_image = get_clipboard_image()

	if clipboard_image:
		return text_from_clipboard_image(clipboard_image, lang)


@eel.expose
def local_files_recognition(lang = "eng"):
	img_names = get_all_images_names()
	return image_text_from_image_folder(img_names, lang)


if __name__ == "__main__":
	eel.start("index.html")