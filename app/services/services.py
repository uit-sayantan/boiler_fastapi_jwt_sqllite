from app.repositories.audit_log import AuditLogRepository
from app.services.user_registration import UserRegistrationService
from app.repositories.user_registration import UserRegistrationRepository

from app.services.user_authentication import UserAuthenticationtService
from app.repositories.user_authentication import UserAuthenticationRepository
from app.services.user_security import UserSecurityService
from app.repositories.user_security import UserSecurityRepository
def get_services():
    user_id = 123
    audit_repo = AuditLogRepository()
    user_registration_repo=UserRegistrationRepository()
    user_auth_repo = UserAuthenticationRepository()
    user_security_repo = UserSecurityRepository()


    user_registration_service = UserRegistrationService(user_registration_repo, audit_repo, user_id)
    user_auth_service = UserAuthenticationtService(user_auth_repo,audit_repo,user_id)
    user_security_service = UserSecurityService(user_security_repo,audit_repo,user_id)
    
    return {
        "user_registration": user_registration_service,
        "user_auth": user_auth_service,
        "user_security": user_security_service
    }
