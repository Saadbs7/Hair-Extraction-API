from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from Segmenter import evaluate
from HairExtractor import extractHair
import cv2 as cv

app = FastAPI()

@app.get("/")
def home():
    return {"Please Go to: http://127.0.0.1:8000/docs#/"}

@app.post("/HairExtraction/upload")
# Define a function to get an image from User
async def UploadImage(file: bytes = File(...)):
    with open('files\input.jpg','wb') as image:
        image.write(file)
        image.close()

    eval = evaluate()
    extr = extractHair()

    return 'Uploaded! ' + eval + extr

@app.get("/HairExtraction/download")
async def download_file(filename: str = "files/output.jpg"):
    return FileResponse('files\output.jpg')