import psycopg2
from app.domain.models import SecurityQuestion,SecurityQuestionList,AuthenticatedUser, UserRole, UserRoleList
from app.domain.enums import UserAuth
from app.config.db import get_conn, release_conn
from app.domain.enums import DbTable,DbView,UserAuth,UiMessage,SecretKeyName
from app.api import models
from app.utils.common_utils import PasswordHash, SkillRampSecret
import pandas as pd
from datetime import datetime

class UserSecurityRepository:
    
    def add_secret_answer_user(self, security_answer):
        try:
            conn = get_conn()
            cur = conn.cursor()
            
            cur.execute(
                f"""delete from {DbTable.USER_SECURITY_QUESTION_ANSWER.value} where emp_id={security_answer.emp_id};"""
            )
            cur.execute(
                f"""insert into {DbTable.USER_SECURITY_QUESTION_ANSWER.value} (emp_id, question_id, answer) values 
                ({security_answer.emp_id}, {security_answer.question_id_1}, '{PasswordHash.get_hash_value(security_answer.answer_1)}'),
                ({security_answer.emp_id}, {security_answer.question_id_2}, '{PasswordHash.get_hash_value(security_answer.answer_2)}');"""
            )
            conn.commit()
            cur.close()
            return models.UiMessageModel(ui_message=UiMessage.SUCCESS.value)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)
    
    def changePassword(self, change_pwd):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select emp_id, password, is_default_password from {DbTable.USER_PASSWORD.value} where emp_id={change_pwd.emp_id}"
            cur.execute(sql)
            row = cur.fetchone()
            sql = f"select date_of_joining from {DbTable.USER_DETAILS.value} where emp_id={change_pwd.emp_id}"
            cur.execute(sql)
            date_of_joining_row = cur.fetchone()
            if row:
                pwd = row[1]
                is_default_password =  row[2]
                doj = date_of_joining_row[0]
                if PasswordHash.compare_hash(change_pwd.old_password, pwd):
                    
                    cur.execute(f"UPDATE {DbTable.USER_PASSWORD.value} SET password = '{PasswordHash.get_hash_value(change_pwd.new_password)}', is_default_password = False WHERE emp_id = {change_pwd.emp_id}")
                    if is_default_password == True and doj == None:
                        cur.execute(f"UPDATE {DbTable.USER_DETAILS.value} SET date_of_joining = '{datetime.now()}' WHERE emp_id = {change_pwd.emp_id}")
                    conn.commit()
                    cur.close()
                    return models.UiMessageModel(ui_message=UiMessage.PWD_CHANGE_SUCCESS.value)
                else:
                    return models.UiMessageModel(ui_message=UiMessage.PWD_NOT_MATCH.value)
            return models.UiMessageModel(ui_message=UiMessage.USER_NOT_FOUND.value)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)
    
    def setSecurityQuestions(self, user_answer):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select emp_id, password from {DbTable.USER_PASSWORD.value} where emp_id={user_answer.emp_id}"
            cur.execute(sql)
            row = cur.fetchone()
            if row:
                pwd = row[1]
                if PasswordHash.compare_hash(user_answer.password, pwd):
                    cur.execute(f"delete from {DbTable.USER_SECURITY_QUESTION_ANSWER.value} where emp_id={user_answer.emp_id};")
                    
                    cur.execute(
                    f"""insert into {DbTable.USER_SECURITY_QUESTION_ANSWER.value} (emp_id, question_id, answer) values 
                    ({user_answer.emp_id}, {user_answer.question_id_1}, '{PasswordHash.get_hash_value(user_answer.answer_1)}'),
                    ({user_answer.emp_id}, {user_answer.question_id_2}, '{PasswordHash.get_hash_value(user_answer.answer_2)}');"""
                    )
                    conn.commit()
                    cur.close()
                    return models.UiMessageModel(ui_message=UiMessage.SECURITY_ANSWER_CHANGE_SUCCESS.value)
                else:
                    return models.UiMessageModel(ui_message=UiMessage.PWD_NOT_MATCH.value)
            return models.UiMessageModel(ui_message=UiMessage.USER_NOT_FOUND.value)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)
    
    def getUser(self, emp_id):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select emp_id, emp_name, role_id,role_name,is_default_password,is_approved from {DbView.USER_DETAILS_V.value} where emp_id={emp_id}"
            cur.execute(sql)
            row = cur.fetchone()

            user = AuthenticatedUser("","",-1,"",None,None)
            if row:
                user = AuthenticatedUser(row[0],row[1],row[2],row[3],row[4],row[5])
            return user
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)


    def update_default_password_by_manager(self, requester_emp_id:int, emp_id:str):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(f"UPDATE {DbTable.USER_PASSWORD.value} SET password = '{PasswordHash.get_hash_value(SkillRampSecret.get_secret(SecretKeyName.PASSWORD.value))}', is_default_password = True WHERE emp_id in ({emp_id})")
            conn.commit()
            cur.close()
            return models.UiMessageModel(ui_message=UiMessage.PWD_CHANGE_SUCCESS.value)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)