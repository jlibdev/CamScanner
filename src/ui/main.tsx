import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import Erro404Page from "../pages/ErrorPage.tsx";
import CapturePage from "../pages/CapturePage.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <HashRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/capture" element={<CapturePage />} />
        <Route path="*" element={<Erro404Page />} />
      </Routes>
    </HashRouter>
  </StrictMode>
);
