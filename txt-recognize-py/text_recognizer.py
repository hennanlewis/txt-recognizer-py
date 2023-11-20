from PIL import ImageGrab
import cv2
import os
import platform
import pygame
import pyperclip
import pytesseract
import time


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

def get_clipboard_image():
	return ImageGrab.grabclipboard()

def text_from_clipboard_image(clipboard_image):
		check_image_folder_exist()
		clipboard_image_name = f"image_{str(time.time())}.jpg"
		clipboard_image.save(f"./{IMG_PATH}/{clipboard_image_name}")
		clipboard_image_text = recognize_text(clipboard_image_name)
		os.remove(f"./{IMG_PATH}/{clipboard_image_name}")
		pyperclip.copy(clipboard_image_text)
		print(f"\n{clipboard_image_text}\n")
		return clipboard_image_text

def execution_end_sound():
	pygame.init()
	pygame.mixer.music.load("./sound/finished.mp3")
	pygame.mixer.music.play()

	# Aguarda até que a reprodução de áudio termine
	while pygame.mixer.music.get_busy():
		pygame.time.delay(100)

	pygame.quit()

def recognize_text(image_full_name, lang="en"):
	image = cv2.imread(f"./{IMG_PATH}/{image_full_name}")
	if OS_NAME == "Windows":
		pytesseract.pytesseract.tesseract_cmd = TESSERACT_WINDOWS_PATH
	text = pytesseract.image_to_string(image, lang="por").strip()
	
	return text

def text_delimiter(full_text, delimiter_name):
	start = f"########## {delimiter_name} start ##########"
	end = f"########## {delimiter_name} end ##########"
	return f"{start}\n{full_text}\n{end}"

def image_text_from_image_folder(img_names):
	text = ""
	for index, image_full_name in enumerate(img_names):
		file_text = recognize_text(image_full_name)
		specified_text = text_delimiter(file_text, image_full_name)

		text = specified_text if index == 0 else f"{text}\n\n{specified_text}"

	return text
