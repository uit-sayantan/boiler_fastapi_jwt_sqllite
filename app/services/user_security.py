from datetime import datetime
import json
from typing import List, Optional
from app.repositories.user_authentication import UserAuthenticationRepository
from app.repositories.user_security import UserSecurityRepository
from app.domain.models import SecurityQuestion,SecurityQuestionList, UserCredential, AuthenticatedUser, ChangePassword, ForgetAndChangePassword, UserSecurityAnswer, UserRole, UserRoleList
from app.repositories.audit_log import AuditLogRepository
from app.api import models
from app.domain.enums import AuditAction

class UserSecurityService:
    def __init__(self, user_security_repo: UserSecurityRepository, audit_repo: AuditLogRepository, user_id: int):
        self.user_security_repo = user_security_repo
        self.audit_repo = audit_repo
        self.user_id = user_id
    
    def add_secret_answer_user(self, security_answer: models.UserSecretAnswerRegister) -> models.UiMessageModel:
        try:
            ui_message = self.user_security_repo.add_secret_answer_user(security_answer)
            self.audit_repo.create({
              'requester_emp_id': self.user_id,
              'action': AuditAction.CREATE.value,
              'object_type': 'user_security_question_answer',
              'object_id': self.user_id,
              'details': json.dumps({'requester_emp_id': self.user_id})
            })
            return ui_message
        except Exception as e:
            print(f"Service error: {e}")
            raise
    
    def change_password(self, change_pwd: ChangePassword) -> models.UiMessageModel:
        try:
            status = self.user_security_repo.changePassword(change_pwd)
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
    
    def set_security_questions(self, user_answer: UserSecurityAnswer) -> models.UiMessageModel:
        try:
            status = self.user_security_repo.setSecurityQuestions(user_answer)
            self.audit_repo.create({
              'requester_emp_id': self.user_id,
              'action': AuditAction.UPDATE.value,
              'object_type': 'user_security_question_answer',
              'object_id': self.user_id,
              'details': json.dumps({'requester_emp_id': self.user_id})
            })
            return status
        except Exception as e:
            print(f"Service error: {e}")
            raise
    
    def get_user(self, id: str) -> AuthenticatedUser:
        try:
            user = self.user_security_repo.getUser(id)
            return user
        except Exception as e:
            print(f"Service error: {e}")
            raise

    def update_default_password_by_manager(self, requester_emp_id:int, emp_id:str) -> models.UiMessageModel:
        try:
            status = self.user_security_repo.update_default_password_by_manager(requester_emp_id=requester_emp_id, emp_id=emp_id)
            self.audit_repo.create({
              'requester_emp_id': self.user_id,
              'action': AuditAction.UPDATE.value,
              'object_type': 'user_password',
              'object_id': emp_id,
              'details': json.dumps({'emp_id': emp_id})
            })
            return status
        except Exception as e:
            print(f"Service error: {e}")
            raise
    
    
    
    