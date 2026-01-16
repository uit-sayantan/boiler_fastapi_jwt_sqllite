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
    services.user_id=body_input.emp_id
    try:
        ui_message = services.user_registration(body_input.emp_id, body_input.emp_name, body_input.email_id,
         body_input.location_id, body_input.lob_id, body_input.learning_plan_id, body_input.specialization_id, body_input.role_id,body_input.tl_emp_id,
         body_input.password,body_input.question_id_1,body_input.answer_1,body_input.question_id_2,body_input.answer_2)
        return ui_message

    except UserExists as e:
        print(f"API error: {e}")
        print(type(e))
        raise HTTPException(status_code=403, detail=(e.msg))

    except Exception as e:
        print(f"API error: {e}")
        raise HTTPException(status_code=500, detail=("something went wrong"))

