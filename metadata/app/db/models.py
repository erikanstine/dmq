from .sqlite import execute_query, fetch_all, fetch_one


class Queue:
    @staticmethod
    def create(name, queue_type, ttl_seconds, max_size):
        query = (
            "INSERT INTO queues (name, type, ttl_seconds, max_size) VALUES (?, ?, ?, ?)"
        )
        execute_query(query, (name, queue_type, ttl_seconds, max_size))

    @staticmethod
    def get_by_id(queue_id):
        query = "SELECT * FROM queues WHERE id = ?"
        return fetch_one(query, (queue_id,))

    @staticmethod
    def list_all():
        query = "SELECT * FROM queues"
        return fetch_all(query)


class Message:
    @staticmethod
    def enqueue(queue_id, content):
        query = "INSERT INTO messages (queue_id, content) VALUES (?, ?)"
        execute_query(query, (queue_id, content))

    @staticmethod
    def list_by_queue(queue_id):
        query = "SELECT * FROM messages WHERE queue_id = ?"
        return fetch_all(query, (queue_id,))

    @staticmethod
    def update_status(message_id, status):
        query = "UPDATE messages SET status = ? WHERE id = ?"
        execute_query(query, (message_id, status))
