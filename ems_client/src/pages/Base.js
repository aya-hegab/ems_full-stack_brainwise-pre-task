import React, { useEffect, useState } from "react";
// import { axiosInstance } from "../apis/config";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";
// import { Link } from "react-router-dom";
// import { clearAllListeners } from "@reduxjs/toolkit";

const Base = () => {
  const navigate = useNavigate();
  useEffect(() => {
    const token = Cookies.get("token");
    const role = Cookies.get("role");

    if (role === "admin") {
      navigate("/base");
    } else {
      navigate("/");
    }
  }, [navigate]);
  return (
    <div>
      <h1>First</h1>
    </div>
  );
};

export default Base;
