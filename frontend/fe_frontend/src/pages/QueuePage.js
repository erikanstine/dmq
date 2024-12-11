import React from "react";
import QueueDetails from "../components/QueueDetails";
import PublishMessageForm from "../components/PublishMessageForm";

const QueuePage = ({ queueName }) => {
    return (
        <div>
            <h1>Queue: {queueName}</h1>
            <QueueDetails queueName={queueName} />
            <PublishMessageForm queueName={queueName} />
        </div>
    );
};

export default QueuePage;