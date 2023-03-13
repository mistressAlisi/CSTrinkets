import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import KnightsTour from './KnightsTour';
import Landing from './Landing';
import MatrixMadness from './MatrixMadness';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
 <BrowserRouter>
      <Routes>
        <Route path="/" >
          <Route index element={<Landing />} />
          <Route path="KnightsTour/" element={<KnightsTour />} />
          <Route path="MatrixMadness/" element={<MatrixMadness />} />
        </Route>
      </Routes>
</BrowserRouter>
  </React.StrictMode>
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
