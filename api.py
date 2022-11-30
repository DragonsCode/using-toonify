from fastapi import BackgroundTasks, FastAPI, Request, Response, Form
from fastapi.middleware.cors import CORSMiddleware
import logging


from tonify import get_image


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post("/photo")
async def photo(filename: str = Form(...), filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    return get_image(image_as_bytes)
    try:
        with open("uploaded_" + filename, "wb") as f:
            f.write(img_recovered)
    except Exception:
        return {"message": "There was an error uploading the file"}
        
    # return {"message": f"Successfuly uploaded {filename}"} 
    return get_image(photo)

@app.post("/set_partners")
async def set_partners(partners):
    try:
        txt = open('partners.txt', 'w')
        txt.write(str(partners))
        txt.close
    except Exception as e:
        logging.info(e)
        return {"ok": False, "message": str(e)}
    return {"ok": True, "message": "Successfully set"}

@app.get("/get_partners")
async def get_partners():
    partners = None
    try:
        txt = open('partners.txt', 'r')
        partners = txt.read()
        txt.close()
    except Exception as e:
        logging.info(e)
        return {"ok": False, "message": str(e)}
    return {"ok": True, "message": "Successfully retrieved", "partners": partners}
