import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
// import { axiosInstance } from "../apis/config";
import Cookies from "js-cookie";
// import { Link } from "react-router-dom";
// import { clearAllListeners } from "@reduxjs/toolkit";

const Login = () => {
  const [loginForm, setLoginForm] = useState({
    username: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = Cookies.get("token");
    const role = Cookies.get("role");
    if (token) {
      if (role === "admin") {
        navigate("/base");
      } else {
        console.log(role);
      }
    }
  }, [navigate]);

  const handleFieldChange = (event) => {
    const field_name = event.target.name;
    const field_value = event.target.value;

    setLoginForm({
      ...loginForm,
      [field_name]: field_value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://127.0.0.1:8000/api/login/", loginForm)
      .then((res) => {
        // console.log(res.data);
        // const { role } = res.data.role;

        if (res.data.role === "admin") {
          Cookies.set("token", res.data.token);
          Cookies.set("role", res.data.role);
          navigate("/base");
        } else {
          setErrorMessage("You ain't an admin");
        }

        // if (user.is_superuser === true) {
        //   navigate("/admin");
        // } else if (user.usertype === "customer") {
        //   navigate("/CustomerProfile", { state: { user, token } });
        // } else if (user.usertype === "vendor") {
        //   navigate("/VendorProfile", { state: { user, token } });
        // } else if (user.usertype === "DeliveryMan") {
        //   navigate("/DeliveryMan", { state: { user, token } });
        // }
      })
      .catch((err) => {
        console.log(err.response);
        if (err.response && err.response.status === 400) {
          setErrorMessage("Invalid email or password. Please try again.");
        } else {
          setErrorMessage("An error occurred. Please try again.");
        }
      });
  };

  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col-md-6 offset-md-3">
            <h2 className="text-center text-dark mt-5">Login Form</h2>
            <div className="text-center mb-5 text-dark">
              Made with bootstrap
            </div>
            <div className="card my-5">
              <form
                className="card-body cardbody-color p-lg-5"
                onSubmit={handleSubmit}
              >
                <div className="text-center">
                  <img
                    src="https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397__340.png"
                    className="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"
                    width="200px"
                    alt="profile"
                  />
                </div>
                {/* <form > */}
                <div className="mb-3">
                  <input
                    type="text"
                    className="form-control"
                    id="Username"
                    aria-describedby="emailHelp"
                    placeholder="Email"
                    onChange={handleFieldChange}
                    name="username"
                  />
                </div>
                <div className="mb-3">
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    placeholder="password"
                    onChange={handleFieldChange}
                    name="password"
                  />
                </div>
                <div className="text-center">
                  <button
                    type="submit"
                    className="btn btn-color px-5 mb-5 w-100"
                  >
                    Login
                  </button>
                </div>
                {/* </form> */}
                <div
                  id="emailHelp"
                  className="form-text text-center mb-5 text-dark"
                >
                  {errorMessage && (
                    <span className="text-danger">{errorMessage}</span>
                  )}
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
