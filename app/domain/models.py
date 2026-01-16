from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Union
from datetime import datetime

@dataclass   
class UserDetails:
    emp_id : Optional[int] = int
    emp_name : Optional[str] = None
    email_id : Optional[str] = None
    location : Optional[str] = None
    lob_id : Optional[str] = None
    learning_plan_id : Optional[str] = None
    specialization_id : Optional[str] = None
    role_id : Optional[str] = None

@dataclass
class SecurityQuestion:
    question_id: Optional[int] = int
    question: Optional[str] = str

@dataclass
class SecurityQuestionList:
    question_list: Optional[List[SecurityQuestion]] = None

@dataclass
class AuthenticatedUser:
    emp_id: int  = None
    name: Optional[str] = None
    role_id: Optional[int] = None
    role_name: Optional[str] = None
    is_first_login: Optional[bool] = None
    is_approved: bool = None

@dataclass
class UserRole:
    role_id: Optional[int] = int
    role_name: Optional[str] = str

@dataclass
class UserRoleList:
    all_role: Optional[List[UserRole]] = None

@dataclass
class UserCredential:
    emp_id: Optional[int] = int
    password: Optional[str] = str

@dataclass
class ChangePassword:
    emp_id: Optional[int] = int
    old_password: Optional[str] = str
    new_password: Optional[str] = str

@dataclass
class ForgetAndChangePassword:
    emp_id: Optional[int] = int
    question_id: Optional[int] = int
    answer: Optional[str] = str
    new_password: Optional[str] = str

@dataclass
class UserSecurityAnswer:
    emp_id: Optional[int] = int
    password: Optional[str] = str
    question_id_1: Optional[int] = int
    answer_1: Optional[str] = str
    question_id_2: Optional[int] = int
    answer_2: Optional[str] = str

@dataclass
class UserRoleUpdate:
    emp_id: str = None #Union[str, int] if needed
    role_id: Optional[int] = None