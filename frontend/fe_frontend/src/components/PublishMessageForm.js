import React, { useState } from "react";
import { publishMessage } from "../api";


const PublishMessageForm = ({ queueName }) => {
    const [message, setMessage] = useState("");
    const [status, setStatus] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await publishMessage(queueName, message);
            setStatus("Message published successfully!");
            setMessage("");
        } catch (err) {
            setStatus(`Error: ${err.message}`);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Message:
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    required
                />
            </label>
            <button type="submit">Publish</button>
            {status && <p>{status}</p>}
        </form>
    );
};

export default PublishMessageForm;