import psycopg2
import pandas as pd
from datetime import date, datetime 
from app.config.db import get_conn, release_conn
from fastapi import HTTPException, status
from app.domain.enums import DbTable,UserAuth,UiMessage,UserDetailsExcelColumn,UserRole
from app.utils.common_utils import PasswordHash
from app.api import models
from app.domain.exception import UserExists

class UserRegistrationRepository:

    def user_registration(self,emp_id:int,emp_name:str,email_id:str,location_id:int,lob_id:int,learning_plan_id:int,
                            specialization_id:int,role_id:int,tl_emp_id:int,password:str,question_id_1:str,
                            answer_1:str,question_id_2:str,answer_2:str):
        
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(f"SELECT 1 FROM {DbTable.USER_DETAILS.value} WHERE emp_id={emp_id}")
            if cur.fetchone():
                raise UserExists(emp_id)
            if learning_plan_id == None:
                learning_plan_id="null"
            if specialization_id == None:
                specialization_id="null"
            if tl_emp_id == None:
                tl_emp_id="null"

            cur.execute(
                        f"""INSERT INTO {DbTable.USER_DETAILS.value} (
                                                        emp_id,
                                                        emp_name,
                                                        email_id,
                                                        location_id,
                                                        lob_id,
                                                        learning_plan_id,
                                                        specialization_id,
                                                        role_id,
                                                        date_of_joining) 
                                    VALUES ({emp_id}, 
                                            '{emp_name}', 
                                            '{email_id}', 
                                            {location_id}, 
                                            {lob_id},
                                            {learning_plan_id}, 
                                            {specialization_id}, 
                                            {role_id},
                                            '{datetime.now()}') """)

            
            cur.execute(
                f"INSERT INTO {DbTable.USER_ORGANIZATION.value} (emp_id,tl_emp_id) VALUES ({emp_id}, {tl_emp_id})")
            hashed_password = PasswordHash.get_hash_value(password)

            cur.execute(
                f"INSERT INTO {DbTable.USER_PASSWORD.value} (emp_id,password,is_default_password) VALUES ({emp_id},'{hashed_password}',false)")
            
            cur.execute(
                    f"""insert into {DbTable.USER_SECURITY_QUESTION_ANSWER.value} (emp_id, question_id, answer) values 
                    ({emp_id}, {question_id_1}, '{PasswordHash.get_hash_value(answer_1)}'),
                    ({emp_id}, {question_id_2}, '{PasswordHash.get_hash_value(answer_2)}')"""
                    )
     
            conn.commit()
            cur.close()
            return models.UiMessageModel(ui_message=UiMessage.SUCCESS.value)

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)

