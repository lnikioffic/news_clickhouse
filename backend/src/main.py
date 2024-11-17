from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.router import router as router_news


app = FastAPI()
app.include_router(router_news)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
