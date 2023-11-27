const startRecognitionButton = document.querySelector("#startRecognitionButton")
const clipboardCheckbox = document.querySelector("#clipboard")
const selectedLanguage = document.querySelector("#language")
const pathButton = document.querySelector("#path-button")
const pathInput = document.querySelector("#path-input")
const result = document.querySelector("#result")

const soundNotification = new Audio("/sound/finished.mp3")

pathButton.addEventListener("click", async () => {
	eel.selecionar_diretorio()(pyReturn => {
		console.log(pyReturn)
	})
})

startRecognitionButton.addEventListener("click", async (event) => {
	event.target.classList.add("active")
	const pythonFunctionName = clipboardCheckbox.checked ? "clipboard_recognition" : "local_files_recognition"
	const textRecognized = await pythonFunctionToExecute(pythonFunctionName)
	result.value = textRecognized
	soundNotification.play()
	event.target.classList.remove("active")
})

const pythonFunctionToExecute = async (functionName) => {
	return new Promise(resolver => {
		eel[functionName]()((pyReturn) => resolver(pyReturn))
	})
}

