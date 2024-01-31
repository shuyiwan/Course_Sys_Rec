import './Styles/App.css';
import './Styles/index.css';
import Navbar from './Components/Navbar'
import About from './Pages/About'
import Search from './Pages/Search'
import CourseCart from './Pages/CourseCart';
import Home from './Pages/Home'
import {Route, Routes} from 'react-router-dom'
import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import axios from 'axios';


function App() {

  const [ user, setUser ] = useState([]);
  const [ profile, setProfile ] = useState([]);

  const login = useGoogleLogin({
      onSuccess: (codeResponse) => setUser(codeResponse),
      onError: (error) => console.log('Login Failed:', error)
  });

  useEffect(
      () => {
          if (user) {
              axios
                  .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
                      headers: {
                          Authorization: `Bearer ${user.access_token}`,
                          Accept: 'application/json'
                      }
                  })
                  .then((res) => {
                      setProfile(res.data);
                  })
                  .catch((err) => console.log(err));
          }
      },
      [ user ]
  );

  const logOut = () => {
    googleLogout();
    setProfile(null);
  };

  return (
    
    <div className="App">
      <>
        <Navbar/>
        <div>
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/search" element={<Search/>}/>
            <Route path="/coursecart" element={<CourseCart/>}/>
            <Route path="/about" element={<About/>}/>
          </Routes>
        </div>
      </>
      
      <div>
            <h2>React Google Login</h2>
            <br />
            {profile ? (
                <div>
                    <img src={profile.picture} alt="user image" />
                    <h3>User Logged in</h3>
                    <p>Name: {profile.name}</p>
                    <p>Email Address: {profile.email}</p>
                    <br />
                    <br />
                    <button onClick={logOut}>Log out</button>
                </div>
            ) : (
              <button onClick={() => login()}>Sign in with Google 🚀 </button>
            )}
      </div>

      <div className="helloWorld">
        MVP
      </div>
      

    </div>

    
  );
}

export default App;
