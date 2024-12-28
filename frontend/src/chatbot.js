// frontend/src/Chatbot.js

import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async () => {
    try {
      const res = await axios.post('http://localhost:5005/webhooks/rest/webhook', {
        sender: 'user',
        message: message,
      });
      setResponse(res.data[0].text);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>AI Chatbot</h2>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
      <p>{response}</p>
    </div>
  );
};

export default Chatbot;
