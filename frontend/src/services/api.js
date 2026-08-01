import axios from "axios";

const API = axios.create({
  baseURL: "http://13.60.5.21:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;
