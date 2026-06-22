from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Union
from datetime import datetime


@dataclass
class UserCredential:
    user_id: Optional[int] = int
    password: Optional[str] = str

@dataclass
class AuthenticatedUser:
    user_id: int  = None
    user_name: Optional[str] = None
    role_id: Optional[int] = None
    role_name: Optional[str] = None
