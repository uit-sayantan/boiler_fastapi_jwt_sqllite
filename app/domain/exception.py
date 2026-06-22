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
