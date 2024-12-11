import React from "react";
import QueueList from "../components/QueueList";

const Dashboard = ({ navigateToQueue }) => {
    const handleQueueSelect = (queueName) => {
        navigateToQueue(queueName);
    };

    return (
        <div>
            <h1>Queue Dashboard</h1>
            <QueueList onSelectQueue={handleQueueSelect} />
        </div>
    );
};

export default Dashboard;