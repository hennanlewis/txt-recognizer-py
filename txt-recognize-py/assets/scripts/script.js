const startRecognitionButton = document.querySelector("#startRecognitionButton")
const soundNotification = new Audio("/assets/sound/finished.mp3")

startRecognitionButton.addEventListener("click", async (event) => {
	const response = await fetch("/local_files_recognition")
	const { text } = await response.json()

	const result = document.querySelector("#result")
	result.textContent = text
	soundNotification.play()
})