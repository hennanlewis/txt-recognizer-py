const startRecognitionButton = document.querySelector("#startRecognitionButton")
const clipboardCheckbox = document.querySelector("#clipboard")
const selectedLanguage = document.querySelector("#language")
const pathButton = document.querySelector("#path-button")
const pathInput = document.querySelector("#path-input")

const soundNotification = new Audio("/sound/finished.mp3")

pathButton.addEventListener("click", async () => {
	eel.selecionar_diretorio()(pyReturn => {
		console.log(pyReturn)
	})
})

startRecognitionButton.addEventListener("click", async (event) => {
	event.target.classList.add("active")
	const pyFuncToExecution = clipboardCheckbox.checked ? "clipboard_recognition" : "local_files_recognition"
	eel[pyFuncToExecution]()((pyReturn) => {
		const result = document.querySelector("#result")
		result.value = pyReturn
		soundNotification.play()
		event.target.classList.remove("active")
	})
})
