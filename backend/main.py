from fastapi import FastAPI
from http import HTTPStatus
from fastapi.middleware.cors import CORSMiddleware
from src.data_server import best_albums

from src.schemas import (
    Message, AlbumsList
)

app = FastAPI(title="My Favorite Albums")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "server running"}


@app.get("/api/albums", status_code=HTTPStatus.OK, response_model=AlbumsList)
def read_albums():

    albums_list = best_albums()

    return {
            'albums_list': albums_list
    }
