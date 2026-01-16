import psycopg2
from app.domain.models import SecurityQuestion,SecurityQuestionList,AuthenticatedUser, UserRole, UserRoleList
from app.domain.enums import UserAuth
from app.config.db import get_conn, release_conn
from app.domain.enums import DbTable,DbView,UserAuth,UiMessage
from app.api import models
from app.utils.common_utils import PasswordHash

class UserAuthenticationRepository:
    
    def authenticateUser(self, user_cred):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select password, is_default_password from {DbTable.USER_PASSWORD.value} where emp_id={user_cred.emp_id}"
            cur.execute(sql)
            row = cur.fetchone()
            user = AuthenticatedUser(user_cred.emp_id,"",-1,"",None)
            if row:
                pwd = row[0]
                is_first_login = row[1]

                if PasswordHash.compare_hash(user_cred.password, pwd):
                    sql = f"""
                    select emp_name,role_id,role_name from {DbView.USER_DETAILS_V.value} where emp_id={user_cred.emp_id};
                    """
                    cur.execute(sql)
                    emp_row = cur.fetchone()
                    user = AuthenticatedUser(user_cred.emp_id,emp_row[0],emp_row[1],emp_row[2],is_first_login)
            return user
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)
    
    def forgetAndChangePassword(self, change_pwd):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select emp_id from {DbTable.USER_DETAILS.value} where emp_id={change_pwd.emp_id}"
            cur.execute(sql)
            row = cur.fetchone()
            if row:
                sql = f"select emp_id,answer from {DbTable.USER_SECURITY_QUESTION_ANSWER.value} where emp_id={change_pwd.emp_id} and question_id={change_pwd.question_id}"
                cur.execute(sql)
                security_row = cur.fetchone()
                if security_row:
                    if PasswordHash.compare_hash(change_pwd.answer, security_row[1]):
                        cur.execute(f"UPDATE {DbTable.USER_PASSWORD.value} SET password = '{PasswordHash.get_hash_value(change_pwd.new_password)}', is_default_password = False WHERE emp_id = {change_pwd.emp_id}")
                        conn.commit()
                        cur.close()
                        return models.UiMessageModel(ui_message=UiMessage.PWD_CHANGE_SUCCESS.value)
                    else:
                        return models.UiMessageModel(ui_message=UiMessage.SECURITY_ANSWER_MISMATCH.value)
                else:
                        return models.UiMessageModel(ui_message=UiMessage.SECURITY_ANSWER_MISMATCH.value)
            return models.UiMessageModel(ui_message=UiMessage.USER_NOT_FOUND.value)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)
    