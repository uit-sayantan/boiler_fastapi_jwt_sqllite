from fastapi import APIRouter, Depends, HTTPException, Request
from app.api import models
from app.services.services import get_services
from app.domain.models import SecurityQuestionList, UserCredential, AuthenticatedUser, ChangePassword, ForgetAndChangePassword, UserSecurityAnswer, UserRole, UserRoleList
from typing import List
from app.utils.common_utils import OAuthToken
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/user_security/add-secret-answer-user/", response_model=models.UiMessageModel)
def add_secret_answer_user(request: Request, requester_emp_id:int,security_answer: models.UserSecretAnswerRegister, services: dict = Depends(get_services)):
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_emp_id, request)
    user_security.user_id=requester_emp_id
    try:
        return user_security.add_secret_answer_user(security_answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/user_security/change-password/", response_model=models.UiMessageModel)
def change_password(request: Request, requester_emp_id:int,change_pwd: ChangePassword, services: dict = Depends(get_services)):
    """
    This endpoint will do the password change if
    1. Old password gets validated
    """
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_emp_id, request)
    user_security.user_id=requester_emp_id
    try:
        return user_security.change_password(change_pwd)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/user_security/set-security-questions/", response_model=models.UiMessageModel)
def set_security_questions(request: Request, requester_emp_id:int,user_answer: UserSecurityAnswer,services: dict = Depends(get_services)):
    """
    This endpoint will do the Security Question and answer change if
    1. Password gets validated
    """
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_emp_id, request)
    user_security.user_id=requester_emp_id
    try:
        return user_security.set_security_questions(user_answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user_security/get-user-details/", response_model=AuthenticatedUser)
def get_user_details(request: Request, requester_emp_id:int, services: dict = Depends(get_services)):
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_emp_id, request)
    user_security.user_id=requester_emp_id
    try:
        user = user_security.get_user(requester_emp_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/user_security/update_default_password_by_manager/", response_model=models.UiMessageModel)
def update_default_password_by_manager(request: Request, requester_emp_id:int, body_input:models.UpdateUserPasswordByManager, services: dict = Depends(get_services)):
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_emp_id, request)
    user_security.user_id=requester_emp_id
    try:
        user = user_security.update_default_password_by_manager(requester_emp_id, body_input.emp_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

