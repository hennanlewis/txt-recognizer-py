from PIL import ImageGrab
import cv2
import os
import platform
import pyperclip
import pytesseract
import time
import shutil

OS_NAME = platform.system()
IMG_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp"]
TESSERACT_WINDOWS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
IMG_PATH = "images"


def check_image_folder_exist():
	if not os.path.exists(IMG_PATH):
		os.makedirs(IMG_PATH)

def get_all_images_names():
	img_array = []
	check_image_folder_exist()

	for image_name in os.listdir(IMG_PATH):
		if image_name.lower().endswith(tuple(IMG_EXTENSIONS)):
			img_array.append(image_name)
	return img_array

def change_image_path_folder(path):
	global IMG_PATH
	IMG_PATH = path

def get_clipboard_image():
	return ImageGrab.grabclipboard()

def text_from_clipboard_image(clipboard_image, lang="eng"):
	check_image_folder_exist()

	clipboard_image_name = f"image_{str(time.time())}.jpg"
	clipboard_image.save(f"images/{clipboard_image_name}")
	clipboard_image_text = recognize_text(clipboard_image_name, lang)

	os.remove(f"images/{clipboard_image_name}")
	pyperclip.copy(clipboard_image_text)
	return clipboard_image_text

def recognize_text(image_full_name, lang="eng"):
	full_path = os.path.abspath(f"{IMG_PATH}\{image_full_name}")
	_, file_extension = os.path.splitext(image_full_name)
	local_image_path = "images"
	local_image_name = f"image_{str(time.time())}.{file_extension}"
	shutil.copyfile(full_path, f"{local_image_path}/{local_image_name}")

	image = cv2.imread(f"{local_image_path}/{local_image_name}")
	if OS_NAME == "Windows":
		pytesseract.pytesseract.tesseract_cmd = TESSERACT_WINDOWS_PATH
	text = pytesseract.image_to_string(image, lang).strip()
	os.remove(f"{local_image_path}/{local_image_name}")

	return text

def text_delimiter(full_text, delimiter_name):
	start = f"<!-- {delimiter_name} start --/>"
	end = f"<!-- {delimiter_name} end --/>"
	full_text = "\n" if full_text == "" else f"\n{full_text}\n"
	return f"{start}{full_text}{end}"

def image_text_from_image_folder(img_names, lang= "eng"):
	text = ""
	for index, image_full_name in enumerate(img_names):
		file_text = recognize_text(image_full_name, lang)
		specified_text = text_delimiter(file_text, image_full_name)

		text = specified_text if index == 0 else f"{text}\n\n{specified_text}"

	return text
