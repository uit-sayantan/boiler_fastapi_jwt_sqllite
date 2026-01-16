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

class AWS(Enum):
    SECRET_NAME = "skillramp-secret"
    REGION_NAME = "us-east-1"
    SERVICE_NAME = 'secretsmanager'

class SecretKeyName(Enum):
    PASSWORD = "DEFAULT_PASSWORD"
    OATH_KEY = "SECRET_KEY"


class UserAuth(Enum):
    DEFAULT_PASSWORD = "Skillramp@2025"

class DbTable(Enum):
    AUDIT = "audit"
    USER_DETAILS_DATA_BATCHES = "user_details_data_batches"
    LEARNING_STAGE_GRAPH = "learning_stage_graph"
    LEARNING_MATERIAL = "learning_material"
    LEARNING_PROGRESS = "learning_progress"
    STAGE = "stage"
    LEARNING_PLAN = "learning_plan"
    SPECIALIZATION_LIST = "specialization_list"
    LOB = "lob"
    QUESTION_BANK = "question_bank"
    EXAM_DETAILS = "exam_details"
    USER_PASSWORD = "user_password"
    USER_ORGANIZATION = "user_organization"
    USER_DETAILS = "user_details"
    LOCATION = "location"
    USER_ROLE = "user_role"
    ASSESSMENT_SUMMARY = "assessment_summary"
    ASSESSMENT_RESPONSE = "assessment_response"
    SECURITY_QUESTIONS = "security_questions"
    USER_SECURITY_QUESTION_ANSWER = "user_security_question_answer"
    PRE_ONBOARDING_EXAM_DETAILS = "pre_onboarding_exam_details"
    QUESTION_BANK_PRE_ONBOARDING = "question_bank_pre_onboarding"
    DIFFICULTY_LEVEL = "difficulty_level"
    ASSESSMENT_AREA = "assessment_area"
    VMO_EXAM_DETAILS = "vmo_exam_details"
    ASSESSMENT_AREA_GROUP_VMO = "assessment_area_group_vmo"
    ASSESSMENT_AREA_VMO = "assessment_area_vmo"
    QUESTION_BANK_VMO = "question_bank_vmo"

class DbView(Enum):
    LEARNING_PLAN_V = "learning_plan_v"
    LEARNING_PROGRESS_DETAIL_V = "learning_progress_detail_v"
    LEARNING_PATH_GUIDE_V = "learning_path_guide_v"
    STAGE_PLAN_V = "stage_plan_v"
    USER_DETAILS_V = "user_details_v"
    EXAM_RESULT_V = "exam_result_v"
    USER_LEADERBOARD_V = "user_leaderboard_v"
    MANAGERS_DASHBOARD_CANDIDATE_V = "managers_dashboard_candidate_v"
    PRE_ONBOARDING_EXAM_DETAILS_V = "pre_onboarding_exam_details_v"
    EXAM_RESULT_PRE_ONBOARDING_V = "exam_result_pre_onboarding_v"
    EXAM_RESULT_FINAL_SCORE_V = "exam_result_final_score_v"
    EXAM_RESULT_PRE_ONBOARDING_PIVOT_V = "exam_result_pre_onboarding_pivot_v"
    VMO_EXAM_RESULT_FINAL_SCORE_V = "vmo_exam_result_final_score_v"
    VMO_EXAM_DETAILS_V = "vmo_exam_details_v"
    EXAM_RESULT_VMO_PIVOT_V = "exam_result_vmo_pivot_v"
    EXAM_RESULT_VMO_V = "exam_result_vmo_v"
    VMO_QUESTION_ALLOCATION_V = "vmo_question_allocation_v"
    QB_ALLOCATION_VALIDATOR_V= "qb_allocation_validator_v"

class UiMessage(Enum):
    SUCCESS = "The Process is Success"
    FAILED = "The Process is Failed"
    INVALID_GCP_PLAN_ID = "Invalid GCP Learning Plan ID"
    INVALID_GWS_PLAN_ID = "Invalid GWS Learning Plan ID"
    INVALID_FILE = "Invalid file type"
    SPECIALIZATION_REQUIRED = "Specialization required for TSR role at rows:"
    QUESTION_BANK_INSERT = "Total Questions inserted: "
    PWD_CHANGE_SUCCESS = "Password Change successful"
    PWD_NOT_MATCH = "Password did not Match"
    USER_NOT_FOUND = "No User Found!"
    SECURITY_ANSWER_MISMATCH = "Security Answer did not Match"
    SECURITY_ANSWER_CHANGE_SUCCESS = "Security Answer reset successful"
    MAX_EXAM_ATTEMPT = "Maximum exam attempts reached"
    CAPTURE_USER_ANSWER_SUCCESS = "User Answer Captured successful"
    ASSESSMENT_DETAILS_NOT_FOUND = "Assessment details not found for the assessment id"
    USER_ALREADY_EXISTS = "User already exists"
    MANAGER_VIEW_DATA_NOT_FOUND = "Manager Data not found for the stage id and lob id"
    STAGE_DETAILS_NOT_FOUND = "Stage Details Not Found!"
    MANAGER_VIEW_MATERIAL_STATUS_DATA_NOT_FOUND = "Manager View of Material Status data not found for the emp id"
    MANAGER_VIEW_CANDIDATES_DATA_NOT_FOUND = "Manager View of Candidates data not found for the lob id"
    PRE_ONBOARDING_BEGINNER_QUESTIONS_NOT_ENOUGH_AVAILABLE = "Not enough beginner questions available"
    PRE_ONBOARDING_INTERMEDIATE_QUESTIONS_NOT_ENOUGH_AVAILABLE = "Not enough intermediate questions available"
    PRE_ONBOARDING_ADVANCED_QUESTIONS_NOT_ENOUGH_AVAILABLE = "Not enough advanced questions available"
    PRE_ASSESSMENT_QUESTION_ALLOCATION_DATA_NOT_FOUND = "Pre Assessment question allocation data not found for the specialization id"
    PRE_ASSESSMENT_AREA_DATA_NOT_FOUND = "Pre Assessment area data not found"
    PRE_ASSESSMENT_DIFFICULTY_LEVEL_DATA_NOT_FOUND = "Pre assessment difficulty level data not found"
    UPDATE_QUESTION_ALLOCATION_DATA_SUCCESS = "Question Allocation Data Update Successful"
    QUESTION_ALLOCATION_INSERT = "Total Question Allocation inserted: "
    INVALID_INPUT = "Please enter the valid input"
    INSUFFICIANT_QUESTION = "INSUFFICIANT QUESTION"
    DUPLICATE_CORRECT_ANSWER = "DUPLICATE CORRECT ANSWER"
    VMO_QUESTION_ALLOCATION_DATA_NOT_FOUND = "VMO Question allocation data not found"
    NO_EXAM_ID_FOUND = "Exam ID not found"
    UPDATE_VMO_QUESTION_ALLOCATION_DATA_SUCCESS = "Update VMO Question Allocation Success"
    UPDATE_VMO_QUESTION_ALLOCATION_DATA_FAILED = "Update VMO Question Allocation Failed"

class CourseStatus(Enum):
    YTS = "Yet To Start"
    IP = "InProgress"
    DN = "Done"
    P = "Pass"
    F = "Fail"
    NS = "Not Started"
    CMP = "Completed"
    INT = "Interrupted"

class UserDetailsExcelColumn(Enum):
    EMPLOYEE_NAME = "Employee Name"
    EMPLOYEE_ID = "Employee #"
    EMAIL_ID = "Email ID"
    Location = "Location"
    LOB = "Mapped LOB"
    ROLE = "Role"
    SPECIALIZATION = "Specialization"

class UserRole(Enum):
    GCP_LEAD = "GCP Lead"
    GCP_TEAM_MANAGER ="GCP Team Manager"
    GCP_WFM = "GCP WFM"
    LEAD = "Lead"
    OPERATIONS_MANAGER = "Operations Manager"
    QA = "QA"
    SME = "SME"
    TEAM_LEAD = "Team Manager"
    TECHNICAL_MANAGER = "Technical Manager"
    TSR = "TSR"

class QuestionBankColumn(Enum):
    QUESTION_ID = "question_id"
    EXAM_ID = "exam_id"
    QUESTION = "question"
    QUESTION_TYPE = "question_type"
    ANSWER_A = "answer_a"
    ANSWER_B = "answer_b"
    ANSWER_C = "answer_c"
    ANSWER_D = "answer_d"
    CORRECT_ANSWER = "correct_answer"
    ANSWER_EXPLANATION = "answer_explanation"
class SpecializationType(Enum):
    ANY = "ANY"

class InvalidValues(Enum):
    INVALID_INTEGER = -1

class OAuthData(Enum):
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES_30 = 30
    ACCESS_TOKEN_EXPIRE_MINUTES_60 = 60
    ACCESS_TOKEN_EXPIRE_MINUTES_90 = 90
    ACCESS_TOKEN_EXPIRE_MINUTES_120 = 120
    ACCESS_TOKEN_EXPIRE_MINUTES_150 = 150
    ACCESS_TOKEN_EXPIRE_MINUTES_180 = 180

class IsExamPass(Enum):
     FALSE = False 
     TRUE = True

class MaterialStatus(Enum):
    NS = "Not Started"
    IP = "InProgress"
    CMP = "Completed"

class TypeOfGraph(Enum):
     BAR = "Bar"
     PIE = "Pie"
    
class BarDatasetLabel(Enum):
    COMPLETION_PERCENTAGE = "completion_percentage"
    TOTAL_TSR = "total_tsr"

class PieDatasetName(Enum):
      NOT_STARTED = "Not Started"
      IN_PROGRESS = "In Progress"
      COMPLETED = "Completed"

class LeaderBoard(Enum):
    USER_RANK_UPTO = 3

class PreOnboardingCandidateStatusRule(Enum):
    BEGINER_MIN = 1
    BEGINER_MAX = 55
    INTERMEDIATE_MAX = 75
    ADVANCED_MAX = 100

class PreOnboardingAreaLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    OPTIONAL = "Optional"

class PreOnboardingExamDetailsDataFrameColumn(Enum):
    ASSESSMENT_AREA_NAME = "assessment_area_name"
    BEGINNER_QUESTION_REQUIRED = "beginner_question_required"
    INTERMEDIATE_QUESTION_REQUIRED = "intermediate_question_required"
    ADVANCED_QUESTION_REUIRED = "advanced_question_required"

class PreOnboardingQuestionBankColumn(Enum):
    ASSESSMENT_AREAS = "Assessment Areas"
    DIFFICULTY_LEVEL = "Difficulty Level"
    QUESTION_COUNT = "question_count"

class PANDASJOINS(Enum):
    LEFT = "left"
    RIGHT = "right"


class IsValid(Enum):
    FALSE = False
    REASON = "max attempts exceeded"

class ExamType(str, Enum):
    material_exam = "Material Exam"
    pre_assessment_exam = "Pre Assessment Exam"
    vmo_exam = "VMO Exam"

class VmoExamDetailsDataFrameColumn(Enum):
    ASSESSMENT_AREA_GROUP_NAME = "assessment_area_group_name"
    ASSESSMENT_AREA_NAME = "assessment_area_name"
    BEGINNER_QUESTION_REQUIRED = "beginner_question_required"
    INTERMEDIATE_QUESTION_REQUIRED = "intermediate_question_required"
    ADVANCED_QUESTION_REQUIRED = "advanced_question_required"

class VmoQuestionBankColumn(Enum):
    ASSESSMENT_AREA_GROUP = "assessment_area_group"
    ASSESSMENT_AREA = "assessment_area"
    SKILL = "skill"
    QUESTION_COUNT = "question_count"

class VmoExamSkillLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    OPTIONAL = "Optional"
