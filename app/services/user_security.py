from app.repositories.user_security import UserSecurityRepository
from app.domain.models import AuthenticatedUser
from app.repositories.audit_log import AuditLogRepository

class UserSecurityService:
    def __init__(self, user_security_repo: UserSecurityRepository, audit_repo: AuditLogRepository, user_id: int):
        self.user_security_repo = user_security_repo
        self.audit_repo = audit_repo
        self.user_id = user_id
    
    def get_user(self, user_id: str) -> AuthenticatedUser:
        try:
            user = self.user_security_repo.getUser(user_id)
            return user
        except Exception as e:
            print(f"Service error: {e}")
            raise

    
    