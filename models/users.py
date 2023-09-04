from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.event import Event


class User(BaseModel):
    email:EmailStr
    password:str
    events:Optional[List[Event]]
    class Config:
        json_schema_extra: {
            "example": {
                "email": "contact@growthentech.com",
                "password":"strongPassword!!!",
                "event": []
            }
        }
        
class UserSignIn(BaseModel):
    email: EmailStr
    password:str
    class Config:
        json_schema_extra: {
            "example":{
                "email":"contact@growthentech.com",
                "password":"strong"
            }
        }