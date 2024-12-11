from pydantic import BaseModel


class Message(BaseModel):
    queue: str
    message: str
