import React from "react";
import { Routes, Route } from "react-router-dom";
import { Suspense } from "react";

// import Base from "../pages/Base";

// const Cart = React.lazy(() => import("../pages/Cart"));
const Base = React.lazy(() => import("../pages/Base"));
const Login = React.lazy(() => import("../pages/Login"));

const Router = () => {
  return (
    <Suspense fallback={<h5>Loading.........</h5>}>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/base" element={<Base />} />
        {/* <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="productDetails/:id" element={<ProductDetails />} />
          <Route path="ProductList" element={<ProductList />} />
          <Route path="WomanPage" element={<WomanPage />} />
          <Route path="MenPage" element={<MenPage />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/wishlist" element={<Wishlist />} />

          <Route path="checkoutPage" element={<CheckoutPage />} />
          <Route
            path="/customerprofile"
            element={<CustomerProfileProtectedRoute />}
          />
          <Route path="/thannk-you" element={<Thankyou />} />
          <Route path="/Deliveryman" element={<Deliveryman />} />
          <Route path="/contact" element={<ContacePage />} />

          <Route path='Register' element={<Register />} />
        </Route> */}

        {/* <Route path="*" element={<NotFound />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/VerifyOTP" element={<VerifyOTP />} />
        <Route path="/ChangePassword" element={<ChangePassword />} />
        <Route path="/ForgetPassword" element={<ForgetPassword />} />
        <Route path="/ChangeForgetPass" element={<ChangeForgetPass />} />
        <Route path="/message" element={<Message />} />
        <Route path="/deleteProduct/:id" element={<DeleteProduct />} />
        <Route path="/UpdateUser/:id" element={<UpdateUser />} /> */}

        {/* -------------- */}

        {/* <Route path="/UserManagement" element={<UserManagement />} />
        <Route path="/ProductManagement" element={<ProductManagement />} />
        <Route path="/VendorPayment" element={<VendorPayment />} />

        <Route path="/Admin" element={<Admin />} />
        <Route path="/AdminUpdatePro/:id" element={<AdminUpdatePro />} />
        <Route path="/AdminAddPro" element={<AdminAddPro />} /> */}

        {/* ----------------- */}

        {/* <Route element={<DelivaryLayout />}>
          <Route
            path="/deliveryman"
            element={<DeliveryManProfileProtectedRoute />}
          />
          <Route path="/orderdetails/:id" element={<Orderdetails />} />
          <Route path="/delivered" element={<Delivered />} />
          <Route path="/shipped" element={<Shipped />} />
          <Route path="/pending" element={<Pending />} />
        </Route> */}

        {/* ------------------------ */}
      </Routes>
    </Suspense>
  );
};

export default Router;
