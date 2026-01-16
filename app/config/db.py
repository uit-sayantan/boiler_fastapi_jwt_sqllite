# db_connect.py
import os
from psycopg2 import pool
from sqlalchemy.engine.url import make_url
from urllib.parse import unquote
from typing import Tuple

def _parse_connection_params() -> Tuple[str, str, str, str, int]:
    """Parse connection params from DATABASE_URL env var OR individual env vars."""
    
    # Check if DATABASE_URL is set (Cloud Run socket mode)
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        print("Using DATABASE_URL with Cloud SQL socket...")
        url = make_url(database_url)
        
        db_name = url.database or os.getenv("DB_NAME", "")
        db_user = url.username or os.getenv("DB_USER", "")
        db_password = url.password or os.getenv("DB_PASS", "")
        host = url.query.get("host", url.host or os.getenv("DB_HOST", "localhost"))
        port = url.port or 5432
        
        print(f"Parsed DATABASE_URL - DB: {db_name}, Host: {host}:{port}")
        
        if not db_name or not db_user:
            raise ValueError("DATABASE_URL missing database name or username")
        
        return db_name, db_user, db_password, host, port
    
    # Fallback to individual env vars (your existing logic)
    else:
        print("Using individual env vars...")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        port = int(os.getenv("DB_PORT", "5432"))
        
        if not all([db_name, db_user, db_password, host]):
            raise ValueError("Missing required env vars: DB_NAME, DB_USER, DB_PASS, DB_HOST")
        
        return db_name, db_user, db_password, host, port

# Global pool (single instance)
pg_pool = None

def init_pool(minconn: int = 1, maxconn: int = 300):
    """Initialize the global connection pool (call once at startup)."""
    global pg_pool
    
    if pg_pool:
        print("Pool already initialized")
        return
    
    db_name, db_user, db_password, host, port = _parse_connection_params()
    
    print(f"Initializing pool: {db_name}@{host}:{port} (user: {db_user[:3]}..., min={minconn}, max={maxconn})")
    
    pg_pool = pool.SimpleConnectionPool(
        minconn=minconn,
        maxconn=maxconn,
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=host,
        port=port,
    )
    
    print("Connection pool initialized successfully")

def get_conn():
    """Get connection from pool (YOUR EXISTING API - NO CHANGES)."""
    global pg_pool
    if not pg_pool:
        raise RuntimeError("Pool not initialized. Call init_pool() first.")
    conn = pg_pool.getconn()
    return conn

def release_conn(conn):
    """Return connection to pool (YOUR EXISTING API - NO CHANGES)."""
    global pg_pool
    if pg_pool:
        pg_pool.putconn(conn)

def close_pool():
    """Close pool (call on shutdown)."""
    global pg_pool
    if pg_pool:
        pg_pool.closeall()
        print("Connection pool closed")

def pool_status():
    """Get pool status."""
    global pg_pool
    if pg_pool:
        return {
            "used": pg_pool.get_used(),
            "free": pg_pool.get_free(),
            "total": pg_pool.get_maxconn(),
        }
    return {"error": "Pool not initialized"}
