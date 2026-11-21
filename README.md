# Stress Detection

A Flask web app for trying the pre-trained stress text classifier. The project also includes a Jupyter notebook and dataset for analysis.

## Project files

```text
Stress Detection/
├── app.py
├── trained_model.pkl
├── Stress (1).csv
├── stress model.ipynb
├── requirements.txt
└── templates/
    └── index.html
```

`trained_model.pkl` is required to run the web app. Keep it in the project root beside `app.py`.

## Setup

Use Python 3.14 and install the listed packages from the project folder:

```powershell
python -m pip install -r requirements.txt
```

The notebook's text-cleaning cells also need the NLTK English stopwords data:

```powershell
python -m nltk.downloader stopwords
```

## Run the web app

Start Flask from the project folder:

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Keep the terminal running while you use the app. Do not open `templates/index.html` directly or with Live Server; its `/predict` request must go to the Flask server.

If `python` is not available in PowerShell, select the project interpreter in VS Code or run the interpreter by its full path, for example:

```powershell
& "C:\Users\Charles Divine\anaconda3\python.exe" app.py
```

## Prediction endpoint

The page submits a form-encoded `text` field to `POST /predict`. The endpoint returns JSON containing the model's `prediction`.

`app.py` enables Flask debug mode for local development. Disable debug mode before deploying the app.
