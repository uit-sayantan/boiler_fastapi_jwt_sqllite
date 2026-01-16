from fastapi import HTTPException, status
from app.domain.enums import UiMessage
user_exists = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=UiMessage.USER_ALREADY_EXISTS.value
        )

class UserExists(Exception):
    def __init__(self, emp_id, msg=UiMessage.USER_ALREADY_EXISTS.value):
        super().__init__()
        self.emp_id = emp_id
        self.msg = msg

    def __str__(self):
        return f'User ID: {self.emp_id}: {self.msg}'

invalid_input = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=UiMessage.INVALID_INPUT.value
        )

class InvalidInput(Exception):
    def __init__(self, emp_id_input, msg=UiMessage.INVALID_INPUT.value):
        super().__init__()
        self.emp_id_input = emp_id_input
        self.msg = msg

    def __str__(self):
        return f'Invalid Input: {self.emp_id_input}: {self.msg}'

class InsufficientQuestion(Exception):
    def __init__(self, area_group, area, difficulty_level, required_question, reason=UiMessage.INSUFFICIANT_QUESTION.value):
        super().__init__()
        self.area_group = area_group 
        self.area = area 
        self.difficulty_level = difficulty_level 
        self.required_question = required_question 
        self.reason = reason 

    def __str__(self):
        return (
            f"{self.reason} | "
            f"Area Group: {self.area_group}, "
            f"Area: {self.area}, "
            f"Difficulty Level: {self.difficulty_level}, "
            f"Required Question: {self.required_question}"
        )

class DuplicateCorrectAnswer(Exception):
    def __init__(self, question, reason=UiMessage.DUPLICATE_CORRECT_ANSWER.value):
        super().__init__()
        self.question = question 
        self.reason = reason 

    def __str__(self):
        return (
            f"{self.reason} | "
            f"Question: {self.question}"
        )