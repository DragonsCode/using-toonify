from fastapi import BackgroundTasks, FastAPI, Request, Response, Form
from fastapi.middleware.cors import CORSMiddleware
import logging

from vkbottle import PhotoToAlbumUploader
from vkbottle.user import User

from tonify import get_image

token = 'vk1.a.bBk3fc7I4J3TFcBC-dQ_czyfx-GA4WX-cQb1jbVOu5DaO3tQ73lF3eR6BL10wmxfyZkM0blByrEYcRYFGlKwLSpA6jgZ9OSC6Qa5-V4maxgcsUe0RWldUZqndildOlMNCTJh1AqI6_hD73cQsKikjdDMVOdpY3X1jMwn-8FxBsZM0-dg5-DIyFeCCVtPRNen-rOJ8ojSqGjkp1_8QmFg2A'
bot = User(token=token)

app = FastAPI()

origins = [
    "http://localhost:8080"
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post("/photo")
async def photo(filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    ok, b64, message = get_image(image_as_bytes)
    photo = None
    # a = await bot.api.photos.edit_album(album_id=289036918, title='Мультики', description='🧐А как ты будешь выглядеть в мультике?\n✨Узнай тут -> https://vk.com/app51488933')
    # print(a.id)
    # print(a.dict())
    if ok:
        photo_upd = PhotoToAlbumUploader(bot.api)
        photo = await photo_upd.upload(album_id=289036918, paths_like='result.jpeg')
        #await bot.api.wall.post(attachments=[photo])
    return {"ok": ok, "message": message, "photo": photo, 'base64': b64}

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
