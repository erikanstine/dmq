from pydantic import BaseModel
from enum import IntEnum


class TypeEnum(IntEnum):
    FIFO = 1
    PRIORITY = 2
    GENERAL_PURPOSE = 3


class Queue(BaseModel):
    name: str
    type: TypeEnum
    ttl_seconds: int
    max_size: int


class QueueResponse(BaseModel):
    id: int
    name: str
    type: int
    ttl_seconds: int
    max_size: int
    created_at: str
