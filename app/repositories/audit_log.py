import psycopg2
import json
from app.config.sqllite_db import get_conn

class AuditLogRepository:

    def create(self, audit_log):
        try:
            conn = get_conn()
            cur = conn.cursor()
            print(audit_log)
            cur.execute(
                "INSERT INTO audit (user_id,action,object) VALUES (?, ?, ?)",
                (
                    audit_log["user_id"],
                    audit_log["action"],
                    json.dumps(audit_log["object"])
                ),
            )
            conn.commit()
            cur.close()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            conn.close()