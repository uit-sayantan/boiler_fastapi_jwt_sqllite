from pydantic import BaseModel,Field
from typing import Optional,List,Dict,Union
import json
from datetime import datetime,date,timedelta

class Education(BaseModel):
    degree: str = Field(..., description="Education Name")
    institute_name: str = Field(..., description="Institute name")
    year: List[str] = Field(..., description="Completion Year")
    score: List[str] = Field(..., description="Score obtained")

class Token(BaseModel):
    emp_id: int
    access_token: str
    token_type: str
    expiry_in_millisec: int

class TokenData(BaseModel):
    requester_emp_id: int | None = None


class UiMessageModel(BaseModel):
    ui_message: str = None

class LOB(BaseModel):
    lob_id: int = None
    lob_name: str = None

class CreateStage(BaseModel):
    lob_id: int = None
    stage_name: str = None

class Stage(BaseModel):
    stage_id: int = None
    stage_name: str = None

class StageList(BaseModel):
    lob: LOB = None
    stages: List[Stage] = None

class CreateLearningPlan(BaseModel):
    lob_id: int = None
    learning_plan_name: str = None

class LearningPlan(BaseModel):
    learning_plan_id: int = None
    learning_plan_name: str = None

class EmpId(BaseModel):
    emp_id: int

class LearningPlanList(BaseModel):
    lob: LOB = None
    learning_plans: List[LearningPlan] = None

class StageLearningPlan(BaseModel):
    learning_stage_order: int = None
    stage: Stage = None
    allocated_days: int = None

class CreateStageLearningPlan(BaseModel):
    learning_stage_order: int = None
    stage_id: int = None
    allocated_days: int = None

class StageGraph(BaseModel):
    lob: LOB = None
    learning_plan: LearningPlan = None
    stages: List[StageLearningPlan] = None

class CreateStageGraph(BaseModel):
    learning_plan_id: int = None
    stages: List[CreateStageLearningPlan] = None

class CreateSpecialization(BaseModel):
    lob_id: int = None
    specialization_name: str = None

class Specialization(BaseModel):
    specialization_id: int = None
    specialization_name: str = None

class SpecializationList(BaseModel):
    lob: LOB = None
    specializations: List[Specialization] = None

class SecurityQuestion(BaseModel):
    question_id: Optional[int] = int
    question: Optional[str] = str

class SecurityQuestionList(BaseModel):
    question_list: Optional[List[SecurityQuestion]] = None

class UserSecretAnswerRegister(BaseModel):
    emp_id: Optional[int] = int
    question_id_1: Optional[int] = int
    answer_1: Optional[str] = str
    question_id_2: Optional[int] = int
    answer_2: Optional[str] = str

class UserCredential(BaseModel):
    emp_id: Optional[int] = int
    password: Optional[str] = str

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class UserRegistration(BaseModel):
    emp_id: int = None
    emp_name: str = None
    email_id: str = None
    location_id: int = None
    lob_id: int = None
    learning_plan_id: Optional[int] = None
    specialization_id: Optional[int] = None
    role_id: int = None
    tl_emp_id: Optional[int] = None
    password: Optional[str] = str
    question_id_1: Optional[int] = int
    answer_1: Optional[str] = str
    question_id_2: Optional[int] = int
    answer_2: Optional[str] = str

class CaptureUserAnswerResponse(BaseModel):
      message: str
      assessment_id: int
      emp_id: int
      exam_id: int
      exam_score: int
      exam_status: str

class CandidatesView(BaseModel):
    lob_id: int = None
    stage_id: int = None
    specialization_id: int = None

class CandidatesResponse(BaseModel):
    emp_id: int = None
    emp_name: str
    date_of_joining: Optional[date] = None
    stage_name: Optional[str] = None
    specialization_name: Optional[str] = None
    completed_on: Optional[date] = None
    status: Optional[str] = None
    completion_percentage: Optional[int] = None
    days_left: Optional[int] = None
    trainer_empid: Optional[int] = None

class GetLocation(BaseModel):
    location_id: int = None
    location_name: str = None

class UpdateDOJbyManager(BaseModel):
    emp_id: str = None
    date_of_joining: str = None

class UpdateUserPasswordByManager(BaseModel):
    emp_id: str = None

