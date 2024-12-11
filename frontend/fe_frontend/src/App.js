import React, { useState } from "react";
import Dashboard from "./pages/Dashboard";
import QueuePage from "./pages/QueuePage";

function App() {
  const [selectedQueue, setSelectedQueue] = useState(null);

  if (selectedQueue) {
    return <QueuePage queueName={selectedQueue} />;
  }

  return <Dashboard navigateToQueue={setSelectedQueue} />;
}

export default App;