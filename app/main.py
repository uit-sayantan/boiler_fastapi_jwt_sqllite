from fastapi import Depends, FastAPI, HTTPException, status, Request

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import user_authentication
from app.api.endpoints import user_security
from app.api.endpoints import user_registration

from app.utils.common_utils import OAuthToken

from app.config.db import init_pool, close_pool

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_pool()

@app.on_event("shutdown")
def shutdown_event():
    close_pool()


app.include_router(user_registration.router,tags=["user_registration"])
app.include_router(user_authentication.router,tags=["user_authentication"])
app.include_router(user_security.router,tags=["user_security"],dependencies=[Depends(OAuthToken.get_current_user)])

origins = ["*"]

@app.middleware("http")
async def print_origin(request: Request, call_next): 
    origin = request.headers.get("origin") 
    print(f"Origin: {origin}") 
    response = await call_next(request) 
    return response

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE","OPTIONS"],  # Allows all methods
    allow_headers=["Authorization","Accept","User-Agent","Content-Type","Content-Length","Cookie","Referer","Host"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SkillRamp App"}

@app.get("/api/health/")
def read_root():
    return {"message": "Welcome to SkillRamp App at /api/health/"}


