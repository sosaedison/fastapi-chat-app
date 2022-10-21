import "./App.css";
import { useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

const SOCKET = new WebSocket("ws://127.0.0.1:8000/ws");

function App() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [user, setUser] = useState();

  const handleGoogleResponseCallBack = (response) => {
    let userObj = jwt_decode(response.credential);

    fetch(`${process.env.REACT_APP_LOCAL_URL}/user/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        first_name: userObj.given_name,
        last_name: userObj.family_name,
        email: userObj.email,
        profile_img_url: userObj.picture,
      }),
    })
      .then((res) => {
        if (res.ok) {
          setUser(userObj);
          document.getElementById("signInDiv").hidden = true;
        }
      })
      .catch((err) => console.log(err));
  };

  function handleSignOut(event) {
    setUser(null);
    document.getElementById("signInDiv").hidden = false;
  }

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

  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id: process.env.REACT_APP_GOOGLE_CLIENT_ID,
      callback: handleGoogleResponseCallBack,
    });

    google.accounts.id.renderButton(document.getElementById("signInDiv"), {
      theme: "outline",
      size: "large",
    });
  });

  return (
    <div className="App">
      {user && <button onClick={(e) => handleSignOut(e)}>Sign Out</button>}
      <div id="signInDiv"></div>
      {user && (
        <>
          <div>
            <img src={user.picture} alt="User Profile" />
            <h3>{`${user.given_name} ${user.family_name}`}</h3>
          </div>
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
        </>
      )}
    </div>
  );
}

export default App;
