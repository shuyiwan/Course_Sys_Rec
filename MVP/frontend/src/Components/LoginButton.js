import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import '../Styles/App.css';
import '../Styles/Login.css';
import './UserTab.js';
import axios from 'axios';
import UserTab from './UserTab.js';

function LoginButton () {
    const [ user, setUser ] = useState(null);
    const [ profile, setProfile ] = useState(null);

    const login = useGoogleLogin({
        onSuccess: (codeResponse) => setUser(codeResponse),
        onError: (error) => console.log('Login Failed:', error)
    });

    useEffect(() => {
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
        }, [ user ]
    );

    const logOut = () => {
        googleLogout();
        setProfile(null);
    };

    return (
        profile ? (
            <div>
                <UserTab myprofile = {profile} logOut={logOut}/>
            </div>
        ) : (
            <button className='loginButton' onClick={login}>Login</button>
        )
    );
};

export default LoginButton;

