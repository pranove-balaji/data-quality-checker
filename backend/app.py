import os
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from backend.utils.core import data_checker
from backend.utils.summary import generate_summary
from fastapi.staticfiles import StaticFiles

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

app = FastAPI()

# Works if running: uvicorn backend.app:app --reload
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")


for m in genai.list_models():
    print(m.name)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)

        # CSV
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)

        # EXCEL
        elif file.filename.endswith((".xls", ".xlsx")):
            df = pd.read_excel(file.file)

        else:
            return {"error": "Unsupported file format"}

        quality_report = data_checker(df)
        summary = generate_summary(quality_report)

        print("\nQUALITY REPORT:", quality_report)
        print("\nSUMMARY:", summary)

        return {
            "quality_report": quality_report,
            "summary": summary
        }

    except Exception as e:
        print("\n🔥🔥 BACKEND ERROR OCCURRED 🔥🔥")
        print("Error Type:", type(e))
        print("Error Message:", str(e))
        print("----------------------------------------------------\n")
        return {"error": str(e)}

