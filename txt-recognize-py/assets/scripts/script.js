const startRecognitionButton = document.querySelector("#startRecognitionButton")
const clipboardCheckbox = document.querySelector("#clipboard")
const pathButton = document.querySelector("#path-button")
const pathSelection = document.querySelector("#path-selection")
const pathInput = document.querySelector("#path-input")
const language = document.querySelector("#language")
const textarea = document.querySelector("#textarea")

const soundNotification = new Audio("/sound/finished.mp3")

const startProcess = (event) => event.target.classList.add("active")

const finishProcess = (event) => {
	soundNotification.play()
	event.target.classList.remove("active")
}

const pythonFunctionToExecute = async (functionName, args) => {
	return new Promise(resolver => {
		return args ?
			eel[functionName](args)((pyReturn) => resolver(pyReturn))
			:
			eel[functionName]()((pyReturn) => resolver(pyReturn))
	})
}

pathButton.addEventListener("click", async () => {
	await pythonFunctionToExecute("select_folder")
})

clipboardCheckbox.addEventListener("change", (event) => {
	const isChecked = event.currentTarget.checked
	console.log(pathSelection)
	pathSelection.style.display = isChecked ? "none" : "flex"
})

startRecognitionButton.addEventListener("click", async (event) => {
	startProcess(event)
	const pythonFunctionName = clipboardCheckbox.checked ? "clipboard_recognition" : "local_files_recognition"
	const textRecognized = await pythonFunctionToExecute(pythonFunctionName, language.value)
	textarea.value = textRecognized
	finishProcess(event)
})
