from enum import Enum

class Environment(Enum):
    PROD = "prod"
    LOCAL = "local"

class AuditAction(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    MOVE = "move"
    SELECT = "select"
    AUTHENTICATE = "authenticate"
    REGISTER = "register"


class UserAuth(Enum):
    DEFAULT_PASSWORD = "Skillramp@2025"

class DbTable(Enum):
    AUDIT = "audit"
    USERS = "users"
    ROLES = "roles"

class DbView(Enum):
    USER_DETAILS_V = "user_details_v"

class UiMessage(Enum):
    SUCCESS = "The Process is Success"
    FAILED = "The Process is Failed"
    USER_ALREADY_EXISTS = "User already exists!"
    INVALID_INPUT = "Invalid input provided!"

class OAuthData(Enum):
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES_30 = 30
    ACCESS_TOKEN_EXPIRE_MINUTES_60 = 60
    ACCESS_TOKEN_EXPIRE_MINUTES_90 = 90
    ACCESS_TOKEN_EXPIRE_MINUTES_120 = 120
    ACCESS_TOKEN_EXPIRE_MINUTES_150 = 150
    ACCESS_TOKEN_EXPIRE_MINUTES_180 = 180

class SecretKeyName(Enum):
    PASSWORD = "password"
    OATH_KEY = "oauth_key"