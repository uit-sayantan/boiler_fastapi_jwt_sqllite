from io import BytesIO, StringIO
from app.domain.models import UserDetails
from datetime import datetime

from app.domain.enums import AuditAction
from app.repositories.user_registration import UserRegistrationRepository
from app.repositories.audit_log import AuditLogRepository
from typing import List, Dict
import json
from app.api import models


class UserRegistrationService:
    def __init__(self, user_registration_repo: UserRegistrationRepository, audit_repo: AuditLogRepository, user_id: int):
        self.user_registration_repo = user_registration_repo
        self.audit_repo = audit_repo
        self.user_id = user_id

    def user_registration(self,user_id:int,user_name:str,password:str) -> models.UiMessageModel:

        try:
            ui_message = self.user_registration_repo.user_registration(user_id=user_id,user_name=user_name,password=password)
            self.audit_repo.create({
                'user_id': self.user_id,
                'action': AuditAction.REGISTER.value,
                'object': json.dumps({'user_id': user_id, 'user_name': user_name})
            })
            return ui_message
        
        except Exception as e:
            print(f"Service error: {e}")
            raise e


