from typing import List, Dict, Optional
from .base import BaseClient
from pydantic import BaseModel
from enum import IntEnum


class TypeEnum(IntEnum):
    FIFO = 1
    PRIORITY = 2
    GENERAL_PURPOSE = 3


class QueueCreateRequest(BaseModel):
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


class MetadataClient(BaseClient):
    def create_queue(
        self, name: str, queue_type: str, ttl: int, max_size: int
    ) -> QueueResponse:
        payload = QueueCreateRequest(
            name=name, type=TypeEnum(queue_type), ttl_seconds=ttl, max_size=max_size
        ).dict()
        response = self.post("/api/queues", payload)
        return QueueResponse(**response)

    def get_queue(self, queue_id: int) -> Optional[QueueResponse]:
        response = self.get(f"/api/queues/{queue_id}")
        return QueueResponse(**response) if response else None

    def list_queues(self) -> List[QueueResponse]:
        response = self.get("/api/queues")
        return [QueueResponse(**queue) for queue in response]

    def delete_queue(self, queue_id: int):
        self.delete(f"/api/queues/{queue_id}")
