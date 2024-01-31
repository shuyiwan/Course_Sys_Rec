import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter} from "react-router-dom"
import { GoogleOAuthProvider } from '@react-oauth/google';
import './Styles/index.css';
import App from './App';
import './Styles/style.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <GoogleOAuthProvider clientId="11264857835-47gag4nl0cm7f5noogp0iv6pdu39eejf.apps.googleusercontent.com">
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>  
    </React.StrictMode>
  </GoogleOAuthProvider>,
  document.getElementById('root')
);

