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

class TokenData(BaseModel):
    requester_user_id: int | None = None

class UiMessageModel(BaseModel):
    ui_message: str = None





