import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [helloText, setHelloText] = useState("None");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/", {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setHelloText(data);
      })
      .catch((err) => {
        setHelloText("Nothing came back");
      });
  }, []);

  return (
    <div className="App">
      <h1>{helloText}</h1>
    </div>
  );
}

export default App;
