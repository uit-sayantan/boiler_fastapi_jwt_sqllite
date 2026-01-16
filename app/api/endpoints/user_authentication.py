from fastapi import APIRouter, Depends, HTTPException
from app.api import models
from app.services.services import get_services
from app.domain.models import SecurityQuestionList, UserCredential, AuthenticatedUser, ChangePassword, ForgetAndChangePassword, UserSecurityAnswer, UserRole, UserRoleList, UserRoleUpdate
from typing import List
from app.utils.common_utils import OAuthToken
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.domain.enums import OAuthData

router = APIRouter()

@router.post("/user_authentication/authenticate-user/", response_model=models.Token)
async def authenticate_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],services: dict = Depends(get_services),):
    user_auth = services["user_auth"]
    user_auth.user_id=form_data.username
    try:
        user_cred = UserCredential(form_data.username,form_data.password)
        user_details = user_auth.authenticate_user(user_cred)
        if user_details.is_first_login == None:
            return models.Token(emp_id=user_details.emp_id, access_token="", token_type="", expiry_in_millisec=0)
        token = OAuthToken.get_access_token(user_details.emp_id, OAuthData.ACCESS_TOKEN_EXPIRE_MINUTES_180.value)
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/user_authentication/forget-and-change-password/", response_model=models.UiMessageModel)
def forget_and_change_password(change_pwd: ForgetAndChangePassword, services: dict = Depends(get_services)):
    """
    This endpoint will do the password change if
    1. Security Question gets validated
    """
    user_auth = services["user_auth"]
    user_auth.user_id=change_pwd.emp_id
    try:
        return user_auth.forget_and_change_password(change_pwd)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
