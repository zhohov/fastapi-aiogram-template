from pydantic import BaseModel


class Message(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True
        