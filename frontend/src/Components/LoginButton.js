import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import '../Styles/App.css';
import '../Styles/Login.css';
import UserTab from './UserTab.js';
import axios from 'axios';

function LoginButton() {
    const [user, setUser] = useState(null);
    const [profile, setProfile] = useState(null);

    const login = useGoogleLogin({
        onSuccess: (codeResponse) => setUser(codeResponse),
        onError: (error) => console.log('Login Failed:', error)
    });

    useEffect(() => {
        if (user) {
            axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
                headers: {
                    Authorization: `Bearer ${user.access_token}`,
                    Accept: 'application/json'
                }
            })
            .then((res) => {
                setProfile(res.data);
                // In here, I moved localStorage.setItem inside then to ensure profile data is available -> can be used in SearchPageResult.js
                localStorage.setItem("email", res.data.email);
            })
            .catch((err) => console.log(err));
        }
    }, [user]);

    const logOut = () => {
        googleLogout();
        setUser(null); // In here, I clear user state on logout -> so in future we can display home page based on user state
        setProfile(null);
    };

    return profile ? (
        <div>
            <UserTab myprofile={profile} logOut={logOut} />
        </div>
    ) : (
        <button className='loginButton' onClick={login}>Login</button>
    );
}

export default LoginButton;
