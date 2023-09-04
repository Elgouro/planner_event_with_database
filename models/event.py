from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id:int
    title:str
    image:str
    description:str
    tags:List[str]
    location:str

class Config:
    json_schema_extra: {
        "example":{
            "title":"FastApi Book Launch",
            "image":"https://linktomyimage.com/image.png",
            "description":"we will be discussing the contents of the FastAPI book in this event ",
            "tags":["Python", "FastAPI","Book","Launch"],
            "Location":"Google Meet"
        }
    }

