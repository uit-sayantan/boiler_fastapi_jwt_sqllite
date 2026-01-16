import bcrypt
import random
from app.domain.enums import OAuthData
from app.api import models
from datetime import datetime, timedelta, timezone
import jwt
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
# import boto3
# from botocore.exceptions import ClientError
from app.domain.enums import AWS, Environment, UserAuth, OAuthData, SecretKeyName
import json
import os

class SkillRampSecret:

    def get_secret(secret_key):
            run_environment=os.getenv("ENV")
            run_environment = Environment.LOCAL.value #Till the time outbond issue is fixed, we dont want to connect to secret manager now
            if run_environment == Environment.LOCAL.value:
                if secret_key == SecretKeyName.PASSWORD.value:
                    return UserAuth.DEFAULT_PASSWORD.value
                elif secret_key == SecretKeyName.OATH_KEY.value:
                    return OAuthData.SECRET_KEY.value
            """
            else:
                session = boto3.session.Session()
                client = session.client(
                    service_name=AWS.SERVICE_NAME.value,
                    region_name=AWS.REGION_NAME.value
                )
                try:
                    get_secret_value_response = client.get_secret_value(
                    SecretId=AWS.SECRET_NAME.value
                    )
                except ClientError as e:
                        raise e
                else:
                    # Secrets Manager decrypts the secret so plain text is returned
                    if 'SecretString' in get_secret_value_response:
                        return json.loads(get_secret_value_response['SecretString'])[secret_key]
                    else:
                        # If the secret is binary
                        return json.loads(get_secret_value_response['SecretBinary'])[secret_key]
            """


class PasswordHash:

    def get_hash_value( plain_text):
        plain_text = plain_text.encode(encoding='utf-8')
        hashed = bcrypt.hashpw(plain_text, bcrypt.gensalt())
        return hashed.decode()
    
    def compare_hash( plain_text, hashed_value):
        plain_text = plain_text.encode(encoding='utf-8')
        hashed_value = hashed_value.encode(encoding='utf-8')
        if bcrypt.checkpw(plain_text, hashed_value):
            return True
        else:
            return False

class OAuthToken:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user_authentication/authenticate-user/")

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        #encoded_jwt = jwt.encode(to_encode, OAuthData.SECRET_KEY.value, algorithm=OAuthData.ALGORITHM.value)
        encoded_jwt = jwt.encode(to_encode, SkillRampSecret.get_secret(SecretKeyName.OATH_KEY.value), algorithm=OAuthData.ALGORITHM.value)
        return encoded_jwt

    def get_access_token(emp_id: int, access_token_expire_minutes: int) -> models.Token:
        print(f"Generating Auth token for: {emp_id}")
        access_token_expires = timedelta(minutes=access_token_expire_minutes)
        access_token = OAuthToken.create_access_token(data={"emp_id": emp_id}, expires_delta=access_token_expires)
        return models.Token(access_token=access_token, token_type="bearer", emp_id=emp_id, expiry_in_millisec=access_token_expire_minutes * 60 * 1000)
    
    def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SkillRampSecret.get_secret(SecretKeyName.OATH_KEY.value),algorithms=[OAuthData.ALGORITHM.value])
            requester_emp_id = payload.get("emp_id")
            if requester_emp_id is None:
                raise credentials_exception
            token_data = models.TokenData(requester_emp_id=requester_emp_id)
        except InvalidTokenError:
            raise credentials_exception
        return token_data
    
    def verify_token_details(requester_emp_id: int, current_user:models.TokenData):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        if requester_emp_id == current_user.requester_emp_id:
            print("User details verified")
            return True
        else:
            raise credentials_exception
    
    def verify_header_details(requester_emp_id: int, request: Request):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        current_user = OAuthToken.get_current_user(request.headers["authorization"].split(" ")[1])
        return OAuthToken.verify_token_details(requester_emp_id, current_user)


class DateTimeUtil:
    def add_days_wo_week_days(date, days_to_add):
        counter = 0
        while True:
            if counter>=days_to_add:
                break
            else:
                date = date + timedelta(days=(1))
                if date.weekday() in [5,6]:
                    pass
                else:
                    counter = counter + 1
        return date
    
    def convert_str_to_datetime(str_date, input_formt = '%Y-%m-%d %H:%M:%S.%f+05:30'):
        return datetime.strptime(str_date, input_formt)
    
    def convert_datetime_to_str(date, input_formt = '%Y-%m-%d %H:%M:%S.%f'):
        return datetime.strftime(date, input_formt)

