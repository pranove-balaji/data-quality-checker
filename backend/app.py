from fastapi import FastAPI,File,UploadFile
import pandas as pd
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
    
         

