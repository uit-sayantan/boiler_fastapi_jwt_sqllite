from fastapi import APIRouter, Depends, HTTPException, Request
from app.services.services import get_services
from app.domain.models import  AuthenticatedUser
from app.utils.common_utils import OAuthToken

router = APIRouter()


@router.get("/user_security/get-user-details/", response_model=AuthenticatedUser)
def get_user_details(request: Request, requester_user_id:int, services: dict = Depends(get_services)):
    user_security = services["user_security"]
    OAuthToken.verify_header_details(requester_user_id, request)
    user_security.user_id=requester_user_id
    try:
        user = user_security.get_user(user_security.user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
