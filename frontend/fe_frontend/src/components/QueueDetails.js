import React, { useEffect, useState } from "react";
import { fetchQueueDetails } from "../api";

const QueueDetails = ({ queueName }) => {
    const [details, setDetails] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {
        const loadQueueDetails = async () => {
            try {
                const data = await fetchQueueDetails(queueName);
                setDetails(data);
            } catch (err) {
                setError(err.message);
            }
        };
        loadQueueDetails();
    }, [queueName]);

    if (error) return <p>Error: {error}</p>;
    if (!details) return <p>Loading queue details...</p>;

    return (
        <div>
            <h3>Queue: {details.name}</h3>
            <p>Messages:</p>
            <ul>
                {/* {details.messages.map((msg, index) => (
                    <li key={index}>{msg.content}</li>
                ))} */}
            </ul>
        </div>
    );
};

export default QueueDetails;