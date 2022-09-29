import io
from fastapi import FastAPI, Response
import asyncio
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import uvicorn
import os
import subprocess
from PIL import Image

def txt2img(prompt: str):
  subprocess.call("rm -r ./outputs")
  subprocess.call("python ./scripts/txt2img.py --n_samples 1 --prompt "+prompt, shell=True)
  image = Image.open("/workspace/stable-diffusion-webui/repositories/stable-diffusion/outputs/txt2img-samples/grid-0000.png")
  byteIO = io.BytesIO()
  image.save(byteIO, format='PNG')
  return byteIO.getvalue()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/txt2img")
async def dreams(prompt: str):
    return Response(content=txt2img(prompt), media_type="image/png")

@app.get("/status")
async def status():
    return Response(status_code=200)

nest_asyncio.apply()
uvicorn.run(app, port=8000)
