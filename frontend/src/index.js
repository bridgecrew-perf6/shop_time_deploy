import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import axios from "axios";

axios.defaults.validateStatus = (status) => status < 500;

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
