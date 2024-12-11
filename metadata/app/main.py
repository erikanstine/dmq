from fastapi import FastAPI
from .models import Queue, QueueResponse

from .db.sqlite import init_db

from .db.models import Queue as DBQueue
from .db.models import Message as DBMessage

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/api/queues")
def create_queue(queue: Queue):
    DBQueue.create(queue.name, queue.type, queue.ttl_seconds, queue.max_size)

    return {"ok"}


@app.get("/api/queues")
def get_queues() -> list[QueueResponse]:
    res = DBQueue.list_all()
    if res:
        return [QueueResponse(**dict(r)) for r in res]

    return []


@app.get("/api/queues/{queue_id}")
def get_queue(queue_id: int) -> QueueResponse:
    res = DBQueue.get_by_id(queue_id=queue_id)
    return QueueResponse(**dict(res))


@app.delete("/api/queues/{queue_id}")
def delete_queue(queue_id: int):
    DBQueue.delete_by_id(queue_id=queue_id)
    return True


"""
POST /queues/{queue_id}/producers — Register a producer.
POST /queues/{queue_id}/consumers — Register a consumer.
GET /queues/{queue_id}/messages — Retrieve message metadata.
GET /queues/{queue_id}/stats — Get queue statistics and health.
"""
