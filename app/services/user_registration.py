import pandas as pd
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

    def user_registration(self,emp_id:int,emp_name:str,email_id:str,location_id:int,lob_id:int,learning_plan_id:int,
                            specialization_id:int,role_id:int,tl_emp_id:int,password:str,question_id_1:str,
                            answer_1:str,question_id_2:str,answer_2:str ) -> models.UiMessageModel:

        try:
            ui_message = self.user_registration_repo.user_registration(emp_id=emp_id,emp_name=emp_name,email_id=email_id,location_id=location_id,lob_id=lob_id,learning_plan_id=learning_plan_id,
                            specialization_id=specialization_id,role_id=role_id,tl_emp_id=tl_emp_id,password=password,question_id_1=question_id_1,
                            answer_1=answer_1,question_id_2=question_id_2,answer_2=answer_2)
            self.audit_repo.create({
                'requester_emp_id': self.user_id,
                'action': AuditAction.REGISTER.value,
                'object_type': 'user_details',
                'object_id': emp_id,
                'details': json.dumps({'emp_id': emp_id})
            })
            return ui_message
        
        except Exception as e:
            print(f"Service error: {e}")
            raise e


