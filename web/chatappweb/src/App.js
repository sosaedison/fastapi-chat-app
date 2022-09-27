import "./App.css";
import { useState, useEffect } from "react";

const socket = new WebSocket("ws://127.0.0.1:8000/ws");

function App() {
  const [helloText, setHelloText] = useState("None");

  useEffect(() => {
    socket.onopen = () => {
      console.log("Connected to backend!");
    };

    socket.onmessage = (message) => {
      setHelloText(message.data);
    };
  }, []);

  return (
    <div className="App">
      <h1>{helloText}</h1>
    </div>
  );
}

export default App;
