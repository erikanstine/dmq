const API_BASE_URL = "/proxy";

export const fetchQueues = async () => {
    const response = await fetch(`${API_BASE_URL}/queues`);
    return response.json();
};

export const fetchQueueDetails = async (queueId) => {
    const response = await fetch(`${API_BASE_URL}/queues/${queueId}`);
    return response.json();
};

export const publishMessage = async (queueName, message) => {
    const response = await fetch(`${API_BASE_URL}/messages`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({"queue": queueName, "message": message}),
    });
    return response.json();
};