import psycopg2
from app.config.sqllite_db import get_conn
from app.domain.enums import DbTable,UiMessage
from app.api import models
from app.domain.exception import UserExists
from app.utils.common_utils import PasswordHash

class UserRegistrationRepository:

    def user_registration(self,user_id:int,user_name:str,password:str):
        
        try:
            conn = get_conn()
            cur = conn.cursor()
            
            cur.execute(f"SELECT 1 FROM {DbTable.USERS.value} WHERE user_id={user_id}")
            if cur.fetchone():
                raise UserExists(user_id)
            cur.execute(f"SELECT role_id FROM {DbTable.ROLES.value} WHERE role_name='user'")
            role_id = cur.fetchone()
            print(user_id,user_name,password)
            cur.execute(
                        f"""INSERT INTO {DbTable.USERS.value} (
                                                        user_id,
                                                        user_name,
                                                        password,
                                                        role_id)
                                    VALUES ({user_id}, 
                                            '{user_name}', 
                                            '{PasswordHash.get_hash_value(password)}',
                                            {role_id[0]});""")
            conn.commit()
            return models.UiMessageModel(ui_message=UiMessage.SUCCESS.value)

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            cur.close()

