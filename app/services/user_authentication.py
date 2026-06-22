
import json
from app.repositories.user_authentication import UserAuthenticationRepository
from app.domain.models import UserCredential, AuthenticatedUser 
from app.repositories.audit_log import AuditLogRepository
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
                'user_id': self.user_id,
                'action': AuditAction.AUTHENTICATE.value,
                'object': json.dumps({'user_id': self.user_id})
            })
            return user
        except Exception as e:
            print(f"Service error: {e}")
            raise
    
    