from pydantic import BaseModel

class Message(BaseModel):
    message: str

class AlbumModel(BaseModel):
    id: int
    color: str
    genre: list[str]
    title: str
    year: str
    labels: list[str]
    producers: list[str]
    songwriters: list[str]
    artist: str
    cover: str
    art_1: str
    art_2: str
    art_3: str
    short_description: str
    long_description: str
    sales: list[str]
    countries: list[str]

class AlbumsList(BaseModel):
    albums_list: list[AlbumModel]