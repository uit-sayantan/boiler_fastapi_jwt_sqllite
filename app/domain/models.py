from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Union
from datetime import datetime

@dataclass
class JobDescription:
    crm_id: Optional[int] = None
    title: Optional[str] = None 
    role: Optional[str] = None  
    description: Optional[Dict] = None    
    skills: Optional[str] = None 
    experience: Optional[int] = None 
    location: Optional[str] = None 
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None    
    created_by: Optional[str] = None
    id: Optional[int] = None
 
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
class UserRegister:
    name: Optional[str] = str
    email_id: Optional[str] = str
    emp_id: Optional[int] = int
    question_id_1: Optional[int] = int
    answer_1: Optional[str] = str
    question_id_2: Optional[int] = int
    answer_2: Optional[str] = str

@dataclass
class UserCredential:
    emp_id: Optional[int] = int
    password: Optional[str] = str

@dataclass
class UserRole:
    role_id: Optional[int] = int
    role_name: Optional[str] = str

@dataclass
class UserRoleList:
    all_role: Optional[List[UserRole]] = None

@dataclass
class AuthenticatedUser:
    emp_id: int  = None
    name: Optional[str] = None
    role_id: Optional[int] = None
    role_name: Optional[str] = None
    is_first_login: Optional[bool] = None
    is_approved: bool = None

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

@dataclass    
class UpdateUserTlempid:
    emp_id: str = None
    tl_emp_id: int = None 

@dataclass    
class UpdateLobSpecializationIds:
    emp_id: str = None
    lob_id: int = None 
    specialization_id: int = None