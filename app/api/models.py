from pydantic import BaseModel,Field
from typing import Optional,List,Dict,Union
import json
from datetime import datetime,date,timedelta

class UserRegistration(BaseModel):
    user_id: int = None
    user_name: str = None
    password: str = None

class Token(BaseModel):
    user_id: int
    access_token: str
    token_type: str
    expiry_in_millisec: int


##################################################


class TokenData(BaseModel):
    requester_user_id: int | None = None

class UiMessageModel(BaseModel):
    ui_message: str = None
 
class UserId(BaseModel):
    user_id: int

class UserCredential(BaseModel):
    user_id: Optional[int] = int
    password: Optional[str] = str

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str




