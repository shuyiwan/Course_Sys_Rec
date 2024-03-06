import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import '../Styles/App.css';
import '../Styles/Login.css';
import axios from 'axios';
import '../Styles/DropdownTab.css';
import { Link } from 'react-router-dom';

function LoginButton() {
    const [user, setUser] = useState(null);
    const name = localStorage.getItem('name');
    const picture = localStorage.getItem('picture');
    const loginStatus = localStorage.getItem('loginStatus');
    const [authorized, setAuthorized] = useState(loginStatus === "false" ? false : true);

    
    const googleLogin = useGoogleLogin({
        onSuccess: (codeResponse) => setUser(codeResponse),
        onError: (error) => console.log('Login Failed:', error)
    });

    const login =  async () => {
        await googleLogin();
    };

    useEffect(() => {
        //console.log(123)
        if (user) {
            axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
                headers: {
                    Authorization: `Bearer ${user.access_token}`,
                    Accept: 'application/json'
                }
            })
            .then((res) => {
                // In here, I moved localStorage.setItem inside then to ensure profile data is available -> can be used in SearchPageResult.js
                localStorage.setItem("email", res.data.email);
                localStorage.setItem("name", res.data.name);
                localStorage.setItem("picture", res.data.picture);
                localStorage.setItem("loginStatus", "true");
                setAuthorized(true);
            })
            .catch((err) => console.log(err));
        }
    }, [user]);

    const logOut = () => {
        googleLogout();
        setUser(null); 
    };

    const handleClick = () => {
        logOut();
        localStorage.removeItem('email');
        localStorage.removeItem('name');
        localStorage.removeItem('picture');
        localStorage.setItem("loginStatus", "false");
        setAuthorized(false);
    };


    return (authorized) ? (  
        <div> 
            <Link to="/">
            <button className="loginButton" onClick={handleClick}>
                <img src={picture} alt="user pic" className="round-image" />                    
                    {name}, Log Out
            </button> 
            </Link>
        </div>     
    ) : (
        <div>
            <Link to="/">
                <button className="loginButton" onClick={login}>Login</button>
            </Link>
        </div>
    );
}

export default LoginButton;
