import psycopg2
from app.domain.models import SecurityQuestion,SecurityQuestionList,AuthenticatedUser, UserRole, UserRoleList
from app.domain.enums import UserAuth
from app.config.sqllite_db import get_conn
from app.domain.enums import DbTable,DbView,UserAuth,UiMessage
from app.api import models
from app.utils.common_utils import PasswordHash

class UserAuthenticationRepository:
    
    def authenticateUser(self, user_cred):
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select password from {DbTable.USERS.value} where user_id={user_cred.user_id}"
            cur.execute(sql)
            row = cur.fetchone()
            user = AuthenticatedUser(user_cred.user_id,"",-1,"")
            if row:
                pwd = row[0]

                if PasswordHash.compare_hash(user_cred.password, pwd):
                    sql = f"""
                    select user_name,role_id,role_name from {DbView.USER_DETAILS_V.value} where user_id={user_cred.user_id};
                    """
                    cur.execute(sql)
                    emp_row = cur.fetchone()
                    user = AuthenticatedUser(user_cred.user_id,emp_row[0],emp_row[1],emp_row[2])
            return user
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            conn.close()
    