const clipboardCheckbox = document.querySelector("#clipboard")
const startRecognitionButton = document.querySelector("#startRecognitionButton")
const soundNotification = new Audio("/assets/sound/finished.mp3")

startRecognitionButton.addEventListener("click", async (event) => {
	event.target.classList.add("active")

	const url = clipboardCheckbox.checked ? "/clipboard_recognition" : "/local_files_recognition"
	const response = await fetch(url)
	const { text } = await response.json()

	const result = document.querySelector("#result")
	result.value = text
	soundNotification.play()
	event.target.classList.remove("active")
})