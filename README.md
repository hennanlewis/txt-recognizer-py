# txt-recognizer-py
This project focuses on developing a text recognition system capable of extracting text content from images. It leverages the power of OpenCV, an open-source computer vision library, and Tesseract, an OCR (Optical Character Recognition) engine developed by Google.

# Requirements

- Python 3.x installed

> PS: If you are a `Windows` user, please install Tesseract following the instructions provided in [this link](https://github.com/UB-Mannheim/tesseract/wiki) to run its functions properly.

# Installation

1. Clone the repository:

```shell
git clone https://github.com/hennanlewis/txt-recognizer-py.git
```

Navigate to the project directory:

```shell
cd txt-recognizer-py
```

Set up a virtual environment (optional but recommended):

```shell
python -m venv .env
source .env/bin/activate
```

On windows:
```shell
python -m venv .env
.env\Scripts\activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

To conclude the use of the environment, employ the following code:

```shell
deactivate
```

# Usage

Run the `app.py` file. The code will recognize the text in all images on folder `img` and sabe in a `output_file.txt`.

# Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
1. Create a new branch
1. Make your changes
1. Submit a pull request

# License

This project is licensed under the MIT License.
