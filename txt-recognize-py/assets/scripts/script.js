const startRecognitionButton = document.querySelector("#startRecognitionButton")
const clipboardCheckbox = document.querySelector("#clipboard")
const language = document.querySelector("#language")
const pathButton = document.querySelector("#path-button")
const pathInput = document.querySelector("#path-input")
const textarea = document.querySelector("#textarea")

const soundNotification = new Audio("/sound/finished.mp3")

pathButton.addEventListener("click", async () => {
	eel.selecionar_diretorio()(pyReturn => {
		console.log(pyReturn)
	})
})

const startProcess = (event) => event.target.classList.add("active")

const finishProcess = (event) => {
	soundNotification.play()
	event.target.classList.remove("active")
}

const pythonFunctionToExecute = async (functionName, language) => {
	return new Promise(resolver => {
		eel[functionName](language)((pyReturn) => resolver(pyReturn))
	})
}

startRecognitionButton.addEventListener("click", async (event) => {
	startProcess(event)
	const pythonFunctionName = clipboardCheckbox.checked ? "clipboard_recognition" : "local_files_recognition"
	const textRecognized = await pythonFunctionToExecute(pythonFunctionName, language.value)
	textarea.value = textRecognized
	finishProcess(event)
})
