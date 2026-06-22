from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form, Request, status
from app.services.services import get_services
from app.domain.enums import UiMessage
from app.api import models
from app.utils.common_utils import OAuthToken
from app.domain.exception import UserExists

router = APIRouter()

@router.post("/user_registration/user_registration", response_model=models.UiMessageModel)
def user_registration(body_input: models.UserRegistration, services: dict = Depends(get_services)):
    services = services["user_registration"]
    services.user_id=body_input.user_id
    try:
        ui_message = services.user_registration(body_input.user_id, body_input.user_name, body_input.password)
        return ui_message

    except UserExists as e:
        print(f"API error: {e}")
        print(type(e))
        raise HTTPException(status_code=403, detail=(e.msg))

    except Exception as e:
        print(f"API error: {e}")
        raise HTTPException(status_code=500, detail=("something went wrong"))

