from datetime import datetime
import json
from typing import List, Optional
from app.repositories.user_authentication import UserAuthenticationRepository
from app.domain.models import SecurityQuestion,SecurityQuestionList, UserCredential, AuthenticatedUser, ChangePassword, ForgetAndChangePassword, UserSecurityAnswer, UserRole, UserRoleList
from app.repositories.audit_log import AuditLogRepository
from app.api import models
from app.domain.enums import AuditAction

class UserAuthenticationtService:
    def __init__(self, user_authentication: UserAuthenticationRepository, audit_repo: AuditLogRepository, user_id: int):
        self.user_authentication = user_authentication
        self.audit_repo = audit_repo
        self.user_id = user_id
    
    def authenticate_user(self, user_cred: UserCredential) -> AuthenticatedUser:
        try:
            user = self.user_authentication.authenticateUser(user_cred)
            self.audit_repo.create({
              'requester_emp_id': self.user_id,
              'action': AuditAction.AUTHENTICATE.value,
              'object_type': 'user_password',
              'object_id': self.user_id,
              'details': json.dumps({'requester_emp_id': self.user_id})
            })
            return user
        except Exception as e:
            print(f"Service error: {e}")
            raise
    
    def forget_and_change_password(self, change_pwd: ForgetAndChangePassword) -> models.UiMessageModel:
        try:
            status = self.user_authentication.forgetAndChangePassword(change_pwd)
            self.audit_repo.create({
              'requester_emp_id': self.user_id,
              'action': AuditAction.UPDATE.value,
              'object_type': 'user_password',
              'object_id': self.user_id,
              'details': json.dumps({'requester_emp_id': self.user_id})
            })
            return status
        except Exception as e:
            print(f"Service error: {e}")
            raise
    