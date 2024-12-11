from fastapi import Depends, FastAPI
from app.client.metadata_client import MetadataClient

from .models import Message


METADATA_SERVICE_URL = "http://localhost:8080"


def get_metadata_client() -> MetadataClient:
    return MetadataClient(base_url=METADATA_SERVICE_URL)


app = FastAPI()


@app.get("/proxy/queues", tags=["Proxy"])
async def list_queues(client: MetadataClient = Depends(get_metadata_client)):
    queues = client.list_queues()
    return {"queues": [queue.dict() for queue in queues]}


@app.get("/proxy/queues/{queue_id}", tags=["Proxy"])
async def list_queues(
    queue_id: int, client: MetadataClient = Depends(get_metadata_client)
):
    queue = client.get_queue(queue_id=queue_id)
    return queue


@app.delete("/proxy/queues/{queue_id}", tags=["Proxy"])
async def delete_queue(
    queue_id: int, client: MetadataClient = Depends(get_metadata_client)
):
    client.delete_queue(queue_id=queue_id)
    return {"message": f"Queue {queue_id} deleted successfully."}


@app.get("/api/queues")
def get_queues():
    queues = [{"name": "queue1", "size": 100}, {"name": "queue2", "size": 50}]
    return queues


@app.get("/api/queues/{queue_name}")
def get_queue(queue_name):
    queue_details = {"name": queue_name, "messages": [{"id": 1, "content": "Hello"}]}
    return queue_details


@app.post("/api/messages")
def publish_message(message: Message):
    return {"queue_name": message.queue, "message": message.message}
