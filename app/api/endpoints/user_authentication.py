from fastapi import APIRouter, Depends, HTTPException
from app.api import models
from app.services.services import get_services
from app.domain.models import UserCredential
from app.utils.common_utils import OAuthToken
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.domain.enums import OAuthData

router = APIRouter()

@router.post("/user_authentication/authenticate-user/", response_model=models.Token)
async def authenticate_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],services: dict = Depends(get_services),):
    user_auth = services["user_auth"]
    user_auth.user_id=form_data.username
    try:
        user_cred = UserCredential(form_data.username,form_data.password)
        user_details = user_auth.authenticate_user(user_cred)
        print(user_details)
        if user_details.user_name == None or user_details.role_id == None:
            return models.Token(user_id=user_details.user_id, access_token="", token_type="", expiry_in_millisec=0)
        token = OAuthToken.get_access_token(user_details.user_id, OAuthData.ACCESS_TOKEN_EXPIRE_MINUTES_180.value)
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
