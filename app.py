import cv2
import os
import pytesseract
import time
import platform

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
	image = cv2.imread(f"{IMG_PATH}/{image_full_name}")
	if operational_system == "Windows":
		pytesseract.pytesseract.tesseract_cmd = TESSERACT_WINDOWS_PATH
	text = pytesseract.image_to_string(image, lang="por").strip()
	
	return text

def specify_text(file_text, image_full_name):
	start = f"########## {image_full_name} start ##########"
	end = f"########## {image_full_name} end ##########"
	return f"{start}\n{file_text}\n{end}"

if __name__ == "__main__":
	img_names = get_all_images()
	start_time = time.time()

	text = ""
	for index, image_full_name in enumerate(img_names):
		file_text = recognize_text(image_full_name)
		specified_text = specify_text(file_text, image_full_name)

		text = specified_text if index == 0 else f"{text}\n\n{specified_text}"

	end_time = time.time()
	total_time = end_time - start_time

	if text:
		with open("output_file.txt", "w", encoding="utf-8") as file:
			file.write(text)

		print(f"Recognizing total time: {total_time}s")