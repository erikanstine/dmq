import React, { useEffect, useState } from "react";
import { fetchQueues } from "../api";

const QueueList = ({ onSelectQueue }) => {
    const [queues, setQueues] = useState([]);
    const [error, setError] = useState("");

    useEffect(() => {
        const loadQueues = async () => {
            try {
                const data = await fetchQueues();
                setQueues(data.queues|| []);
            } catch (err) {
                setError(err.message);
            }
        };
        loadQueues();
    }, []);

    if (error) return <p>Error: {error}</p>;
    if (!queues.length) return <p>No queues available.</p>;

    return (
        <ul>
            {queues.map((queue) => (
                <li key={queue.name}>
                    <button onClick={() => onSelectQueue(queue.id)}>
                        {queue.name} (max_size: {queue.max_size} - id: {queue.id})
                    </button>
                </li>
            ))}
        </ul>
    );
};

export default QueueList;