from fastapi import APIRouter, status, Request
from domain.message import Message

message_router = APIRouter(
    prefix="/message_router",
    tags=["message_router"],
)


@message_router.get("/", status_code=status.HTTP_200_OK)
async def get(request: Request) -> Message:
    message = Message(
        id=1,
        text="Hello, World!"
    )
    return message
