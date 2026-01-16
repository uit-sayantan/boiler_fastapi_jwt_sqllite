from pydantic import BaseModel,Field
from typing import Optional,List,Dict,Union
import json
from datetime import datetime,date,timedelta

class Education(BaseModel):
    degree: str = Field(..., description="Education Name")
    institute_name: str = Field(..., description="Institute name")
    year: List[str] = Field(..., description="Completion Year")
    score: List[str] = Field(..., description="Score obtained")

class PositionFillStatus(BaseModel):
    requirement_status: List[str] = None
    count: List[int] = None

class UpdateLearningProgressDetails(BaseModel):
    emp_id: int = None
    stage_id : int=None
    material_id : int=None

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

class ContentMaterial(BaseModel):
    material_id: int = None
    topic_name: str = None
    content_link: Optional[str] = None
    exam_id: Optional[int] = None

class ContentMaterialList(BaseModel):
    stage_id: int = None
    specialization_id: int = None
    materials: List[ContentMaterial] = None


class CreateQB(BaseModel):
    stage_id: int = None
    specialization_id: int = None
    material_id: int = None
    exam_name: str = None
    number_of_question_for_exam: int = None

class GenerateExamQuestionRequest(BaseModel):
    emp_id: int = None
    exam_id: int = None

class QuestionList(BaseModel):
    question_order: int = None
    question_id: int = None
    question_area_description: str = None
    question: str = None
    question_type: str = None
    answer_a: str = None 
    answer_b: str = None 
    answer_c: str = None 
    answer_d: str = None 
    correct_answer: str = None 
    answer_explanation: str = None 

class GenerateExamQuestionResponse(BaseModel):
    token: Token = None
    assessment_id: int = None
    questions: List[QuestionList] = None

    
class GetQB(BaseModel):
    stage_id: int = None
    specialization_id: int = None
    material_id: int = None

class ExamDetails(BaseModel):
    exam_id: int = None
    exam_name: str = None
    number_of_question_for_exam: int = None
    pass_percentage: int = None
    max_attempt: int = None

class Question(BaseModel):
    exam_id: int = None
    question_id: int = None
    question: str = None
    question_type: str = None
    answer_a: str = None
    answer_b: str = None
    answer_c: str = None
    answer_d: str = None
    correct_answer: str = None

class QuestionBank(BaseModel):
    exam_details: ExamDetails = None
    question_list: List[Question] = None

class DistinctStage(BaseModel):
    stage_order: int = None
    stage_id: int = None
    stage_name: str = None
    complete_percentage: int = None
    total_material: int = None
    allocated_days:int = None
    end_date: datetime = None

class PreOnboardingDetails(BaseModel):
    exam_id: int = None
    assessment_id: int = None
    is_exam_pass: bool = None

class VmoExamDetails(BaseModel):
    exam_id: int = None
    assessment_id: int = None
    is_exam_pass: bool = None

class UserStageDetails(BaseModel):
    emp_name: str = None
    lob_name: str = None
    learning_plan_name: str = None
    specialization_name: str = None
    tl_emp_id:int = None
    overall_percentage: Optional[float] = None
    pre_onboarding_details: PreOnboardingDetails = None
    vmo_details: VmoExamDetails = None
    stage_details: List[DistinctStage] = None

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

class DisplayLearningDataIP(BaseModel):
    emp_id: int
    stage_id: int = None

class DisplayLearningDataOP(BaseModel):
    material_id: int = None
    topic_name: str = None
    content_link: Optional[str] = None
    exam_id: Optional[int] = None
    content_status: str = None
    content_completed_at: Optional[date] = None
    exam_status: str = None
    exam_completed_at: Optional[date] = None
    material_status: str = None

class UserAnswerList(BaseModel):
    question_order: int
    question_id: int 
    user_answer: str

class CaptureUserAnswerRequest(BaseModel):
    assessment_id: int
    submit_reason: str
    is_final_submit: bool
    user_answers: List[UserAnswerList]

class AssessmentDetailsResponse(BaseModel):
    total_question : int 
    max_attempt : int
    pass_percentage: int
    failed_attempt_count : int

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

class ManagerDashboardRequest(BaseModel):
    lob_id: int = None

class BarDataset(BaseModel):
    label: str = None
    data: List[float] = None

class PieDataset(BaseModel):
    name: str = None
    value: float = None

class PieSpecialization(BaseModel):
    specialization: str = None 
    chart_type: str = None
    datasets: List[PieDataset] = None

class BarStageResponse(BaseModel):
    learning_stage_order: int = None
    stage: str = None
    chart_type: str = None
    labels: List[str] = None 
    datasets: List[BarDataset] = None
    specializations : List[PieSpecialization] = None

class PieStageResponse(BaseModel):
    learning_stage_order: int = None
    stage: str = None
    chart_type: str = None
    datasets: List[PieDataset] = None

class MaterialItem(BaseModel):
      stage_name: str = None
      specialization_name: str = None
      material_id: int = None
      topic_name: str = None
      total_tsr: int = None
      completed_course_count: int = None
      inprogress_course_count: int = None
      not_started_course_count: int = None

class ManagerDashboardChartViewResponse(BaseModel):
    stages: List[Union[BarStageResponse, PieStageResponse]] = None
    materials: List[MaterialItem] = None


class LeaderBoard(BaseModel):
    rank: int= None
    emp_name: str= None
    points: int= None

class LeaderBoardList(BaseModel):
    candidate_rank: int= None
    candidate_score: int= None
    leader_board: List[LeaderBoard]= None

class Emp(BaseModel):
    emp_id: int= None
    emp_name: str= None

class UserDetails(BaseModel):
    emp_id: int
    emp_name: Optional[str] = None
    date_of_joining: Optional[date] = None
    lob_name: Optional[str] = None
    specialization_name: Optional[str] = None

class StageDetails(BaseModel): 
    learning_stage_order: Optional[int] = None 
    stage_name: Optional[str] = None
    duration: Optional[int] = None
    expected_completion: Optional[date] = None
    completed_on: Optional[date] = None
    days_left: Optional[int] = None
    status: Optional[str] = None

class MaterialIteam(BaseModel):
    material_id: Optional[int] = None
    stage_name: Optional[str] = None
    topic_name: Optional[str] = None
    material_status: Optional[str] = None


class CandidatesDetailsResponse(BaseModel):
    user_details: List[UserDetails] = None
    stage_details: List[StageDetails] = None
    material_status: List[MaterialIteam] = None

class PreOnboardingAssessmentDetailResult(BaseModel):
    assessment_area_id: int = None
    assessment_area_name: str = None
    area_difficulty_level_id: int = None
    area_difficulty_level_name: str = None
    beginner_question_attempted: Optional[int] = None
    beginner_correct_answer_count: Optional[int] = None
    beginner_total_question: Optional[int] = None
    beginner_percentage: Optional[int] = None
    intermediate_question_attempted: Optional[int] = None
    intermediate_correct_answer_count: Optional[int] = None
    intermediate_total_question: Optional[int] = None
    intermediate_percentage: Optional[int] = None
    advanced_question_attempted: Optional[int] = None
    advanced_correct_answer_count: Optional[int] = None
    advanced_total_question: Optional[int] = None
    advanced_percentage: Optional[int] = None
    area_percentage: int = None
    area_status: str = None

class PreOnboardingAssessmentQnA(BaseModel):
    question_order: int = None
    question_area_name: str = None
    question_difficulty_level: str = None
    question: str = None
    answer_a: str = None
    answer_b: str = None
    answer_c: str = None
    answer_d: str = None
    correct_answer: str = None
    user_answer: Optional[str] = None
    
    

class PreOnboardingAssessmentResultPercentage(BaseModel):
    assessment_details: List[PreOnboardingAssessmentDetailResult]
    assessment_qna: List[PreOnboardingAssessmentQnA]

class PreOnboardingAssessmentResult(BaseModel):
    emp_name: str = None
    lob: str = None
    assessment_id: int = None
    is_exam_pass: Optional[bool] = None
    specialization: str = None
    final_score: Optional[int] = None
    final_status: Optional[str] = None
    assessment_result : PreOnboardingAssessmentResultPercentage = None

class PreOnboardingExamStatus(BaseModel):
    emp_id: int = None
    assessment_id: int = None
    is_exam_pass: bool = None
    reason: str = None

class InvalidateExamAttempts(BaseModel):
    emp_id: int = None
    assessment_id: int = None
    reason: str = None

class QuestionAllocationData(BaseModel):
    specialization_id: int = None
    specialization_name: str = None 
    assessment_area_id: int = None 
    assessment_area_name:str = None 
    difficulty_level_id:int = None 
    difficulty_level_name:str = None 
    beginner_question_count:int = None
    intermediate_question_count: int = None 
    advanced_question_count:int = None 
    exam_id:int = None 

class AssessmentAreaData(BaseModel):
    assessment_area_id:int = None 
    assessment_area_name:str = None 

class DifficultyLevelData(BaseModel):
    difficulty_level_id:int = None 
    difficulty_level_name:str = None

class QuestionAllocationList(BaseModel):
    assessment_area_id: int = None 
    difficulty_level_id:int = None 
    beginner_question_count:int = None
    intermediate_question_count: int = None 
    advanced_question_count:int = None 

class UpdateQuestionAllocationRequest(BaseModel):
    specialization_id: int = None
    question_allocation_data: List[QuestionAllocationList]

class GetUserDetails(BaseModel):
    emp_id: Optional[int] = None
    emp_name: Optional[str] = None
    email_id: Optional[str] = None
    location_name: Optional[str] = None
    lob_name: Optional[str] = None
    learning_plan_name: Optional[str] = None
    specialization_name: Optional[str] = None
    role_name: Optional[str] = None
    tl_emp_id: Optional[int] = None
    date_of_joining: Optional[date] = None
    is_approved: Optional[bool] = None
    approved_by: Optional[int] = None

class InvalidAssessmentReason(BaseModel):
    invalidated_by: Optional[int] = None
    invalidated_reason: Optional[str] = None
    invalidated_at: Optional[str] = None

class OnboardingAssessmentDetailsResponse(BaseModel):
    specialization_name : str
    emp_id : int
    emp_name :  Optional[str] = None
    assessment_id : Optional[int] = None
    is_valid_assessment: Optional[bool] = None
    invalid_assessment_reason: Optional[InvalidAssessmentReason] = None
    status :  Optional[str] = None
    avg_percentage : Optional[int] = None
    assessment_start_time : Optional[datetime] = None
    duration : Optional[float] = None
    location :  Optional[str] = None

class ExamMetadataResponse(BaseModel):
    exam_name : str 
    number_of_question : int 
    pass_percentage: int
    max_attempt : int
    questions: List[QuestionList]

class OnboardingAssessmentDetailResult(BaseModel):
    assessment_area_id: int = None
    assessment_area_group_name: str = None
    assessment_area_name: str = None
    area_difficulty_level_id: int = None
    area_difficulty_level_name: str = None
    question_attempted: Optional[int] = None
    correct_answer_count: Optional[int] = None
    total_question: Optional[int] = None
    percentage: Optional[int] = None
    

class OnboardingAssessmentResultPercentage(BaseModel):
    assessment_details: List[OnboardingAssessmentDetailResult]

class OnboardingAssessmentResult(BaseModel):
    emp_name: str = None
    lob: str = None
    assessment_id: int = None
    is_valid_assessment: Optional[bool] = None
    is_exam_pass: Optional[bool] = None
    assessment_progress_status :  Optional[str] = None
    specialization: str = None
    final_score: Optional[int] = None
    assessment_result : OnboardingAssessmentResultPercentage = None

class LearnngMaterialForStagexSpecialization(BaseModel):
    stage_id: int = None
    specialization_id: int = None
    material_id: Optional[int] = None
    topic_name: str = None
    content_link: str = None

class UpdateApprovals(BaseModel):
    emp_id: str = None
    is_approved: bool = None
    comment: str = None

class UpdateUserRegistration (BaseModel):
    emp_id: int = None
    emp_name: str = None
    email_id: str = None
    location_id: int = None
    lob_id: int = None
    learning_plan_id: Optional[int] = None
    specialization_id: Optional[int] = None
    role_id: int = None
    tl_emp_id: Optional[int] = None

class ExamId(BaseModel):
    exam_id: int = None

class VMOQuestionAllocationData(BaseModel):
    assessment_area_group_name: str = None
    assessment_area_group_id: int = None
    assessment_area_name: str = None
    assessment_area_id: int = None
    max_beginner_question_count: int = None
    allocated_beginner_question_count:  Optional[int] = int
    max_intermediate_question_count: int = None
    allocated_intermediate_question_count:  Optional[int] = int
    max_advance_question_count: int = None
    allocated_advanced_question_count:  Optional[int] = int

class VMOQuestionAllocationList(BaseModel):
    assessment_area_group_id:int = None
    assessment_area_id: int = None 
    current_beginner_question:int = None
    current_intermediate_question: int = None 
    current_advance_question:int = None 

class UpdateVMOQuestionAllocationRequest(BaseModel):
    specialization_id: int = None
    vmo_question_allocation_data: List[VMOQuestionAllocationList]