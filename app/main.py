from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api, user
from app.db import engine, Base

app = FastAPI(
    max_request_size=10 * 1024 * 1024 # 10MB
)

# Cors Settings;
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

Base.metadata.create_all(bind=engine)

# Add routes
app.include_router(api.router)
app.include_router(user.router)
