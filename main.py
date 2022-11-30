import uvicorn


def start():
    uvicorn.run("api:app", reload=True)


if __name__ == '__main__':
    start()