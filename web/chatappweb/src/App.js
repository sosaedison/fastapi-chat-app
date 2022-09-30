import "./App.css";
import { useState } from "react";

const SOCKET = new WebSocket("ws://127.0.0.1:8000/ws");

function App() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");

  const send_message = (message) => {
    SOCKET.send(inputMessage);
    setInputMessage("");
  };

  const handleChatMessageChange = (e) => {
    setInputMessage(e.target.value);
  };

  const enter_pressed = (e) => {
    if (e.keyCode === 13) {
      send_message(inputMessage);
    }
  };

  SOCKET.onopen = () => {
    console.log("Connected to backend!");
  };

  SOCKET.onmessage = (message) => {
    message = JSON.parse(message.data);
    setMessages([...messages, message.msg]);
  };

  return (
    <div className="App">
      <div id="chat">
        <div id="chat_messages">
          <ul>
            {messages.map((m, i) => {
              return <li key={i}>{m}</li>;
            })}
          </ul>
        </div>
        <div id="chat_input">
          <input
            type="text"
            onChange={handleChatMessageChange}
            onKeyUp={enter_pressed}
            value={inputMessage}
          ></input>
          <button type="submit" onClick={send_message}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
