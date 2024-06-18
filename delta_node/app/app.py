import asyncio
from typing import Any
from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from fastapi.middleware.cors import CORSMiddleware


from .v1 import router as v1_router

# for debug
origins = [
    "http://localhost",
    "http://localhost:5173",
]

app = FastAPI()
app.include_router(v1_router, prefix="/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头
)


async def run(host: str, port: int):
    config = Config()
    config.bind = [f"{host}:{port}"]
    config.accesslog = "-"
    config.errorlog = "-"

    shutdown_event = asyncio.Event()

    try:
        await serve(app, config, shutdown_trigger=shutdown_event.wait)  # type: ignore
    except asyncio.CancelledError:
        shutdown_event.set()
