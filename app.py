import cv2
import os
import pytesseract
import time
import platform
from PIL import ImageGrab, Image

operational_system = platform.system()

IMG_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp"]
TESSERACT_WINDOWS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
IMG_PATH = "images"

def get_all_images():
	img_array = []
	for image_name in os.listdir(IMG_PATH):
		if image_name.lower().endswith(tuple(IMG_EXTENSIONS)):
			img_array.append(image_name)
	return img_array

def recognize_text(image_full_name):
	image = cv2.imread(f"./{IMG_PATH}/{image_full_name}")
	if operational_system == "Windows":
		pytesseract.pytesseract.tesseract_cmd = TESSERACT_WINDOWS_PATH
	text = pytesseract.image_to_string(image).strip()
	
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

def text_from_clipboard_image(clipboard_image):
		clipboard_image_name = f"image_{str(time.time())}.jpg"
		clipboard_image.save(f"./{IMG_PATH}/{clipboard_image_name}")
		clipboard_image_text = recognize_text(clipboard_image_name)
		os.remove(f"./{IMG_PATH}/{clipboard_image_name}")
		print(f"\n\n{clipboard_image_text}\n\n")

if __name__ == "__main__":
	img_names = get_all_images()

	clipboard_image = ImageGrab.grabclipboard()
	if clipboard_image: text_from_clipboard_image(clipboard_image)

	start_time = time.time()
	print(time.time())
	text = image_text_from_image_folder(img_names)
	end_time = time.time()
	total_time = end_time - start_time

	if text:
		with open("output_file.txt", "w", encoding="utf-8") as file:
			file.write(text)

		print(f"Recognizing total time: {total_time}s")