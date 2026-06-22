import psycopg2
from app.domain.models import AuthenticatedUser
from app.config.sqllite_db import get_conn
from app.domain.enums import DbView

class UserSecurityRepository:
    
    def getUser(self, user_id: str) -> AuthenticatedUser:
        try:
            conn = get_conn()
            cur = conn.cursor()
            sql = f"select user_id, user_name, role_id,role_name from {DbView.USER_DETAILS_V.value} where user_id={user_id}"
            cur.execute(sql)
            row = cur.fetchone()

            user = AuthenticatedUser("","",-1,"")
            if row:
                user = AuthenticatedUser(row[0],row[1],row[2],row[3])
            return user
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            conn.close()

