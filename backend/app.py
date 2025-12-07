import os
from fastapi import FastAPI,File,UploadFile
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from utils.core import data_checker
from utils.summary import generate_summary

load_dotenv()

api_key=os.getenv("api_key")
genai.configure(api_key=api_key)
app=FastAPI()
@app.post('/upload/')
async def upload_file(file: UploadFile=File(...)):
    df=None
    if(file.filename.endswith('.csv')):
        df=pd.read_csv(file.file)
    elif file.filename.endswith(('.xls','xslx')):
         df=pd.read_excel(file.file)
    else:
        return {"error":"unsupported file"}
    
    quality=data_checker(df)
    summary=generate_summary(quality)
    return{
        summary
    }
         

