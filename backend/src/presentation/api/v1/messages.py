from fastapi import APIRouter, Request, status

from domain.message import Message

message_router = APIRouter(
    prefix="/messages",
    tags=["messages"],
)


@message_router.get("/", status_code=status.HTTP_200_OK)
async def get(request: Request) -> Message:
    message = Message(id=1, text="Hello, World!")
    return message
