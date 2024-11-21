from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.news.router import router as router_news
from src.tags.router import router as router_tags


app = FastAPI()
app.include_router(router_news)
app.include_router(router_tags)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
