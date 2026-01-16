import psycopg2
import json
from app.config.db import get_conn, release_conn
from datetime import datetime

class AuditLogRepository:

    def create(self, audit_log):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO audit (action, requester_emp_id,object_type, object_id, details) VALUES (%s, %s, %s, %s, %s)",
                (
                    audit_log["action"],
                    audit_log["requester_emp_id"],
                    audit_log["object_type"],
                    audit_log["object_id"],
                    json.dumps(audit_log["details"]),
                ),
            )
            conn.commit()
            cur.close()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise
        finally:
            release_conn(conn)