import '@/components/Login/LoginAndSignUpNode.css'
import {useEffect, useState} from 'react';
import {Mail, KeyRound, User} from 'lucide-react'
import { useNavigate } from "react-router";
import { GetCookie } from "@/utility/HttpUtility.js"

export default function LoginAndSignUpNode({setIsSignedIn}) {
    
    const [isLoginOption, setIsLoginOption] = useState(true);
    const navigate = useNavigate();
    
    let password = "";
    let email = "";
    let username = "";
    
    return (
        <div className="login-and-signup-node">
            <div className = "login-and-signup-options">
              <button 
                  className={isLoginOption ? "login-button-active" : "login-button-inactive"}
                  onClick={() => setIsLoginOption(true)}
              >
                  Login
              </button>
              <button 
                  className={isLoginOption ? "signup-button-inactive" : "signup-button-active"}
                  onClick={() => setIsLoginOption(false)}
              >
                  Sign Up
              </button>
            </div>
            
            <div className="login-and-signup-input-container">
                <div>
                    <div className="simple-flex-container">
                        <User/> <p>User name</p>
                    </div>
                    <input 
                        type="text" 
                        placeholder="Type Username" 
                        onChange={(val) => username = val.target.value}
                    />
                </div>
                {
                    isLoginOption ? null : 
                    <div>
                        <div className="simple-flex-container">
                            <Mail/> <p>Email</p>
                        </div>
                        
                        <input 
                            type="text"
                            placeholder="Type Email"
                            onChange={(val) => email = val.target.value}
                            />
                    </div>
                }
                <div>
                    <div className="simple-flex-container">
                        <KeyRound/> <p>Password</p>
                    </div>
                    <input 
                        type="text"
                        placeholder="Type Password"
                        onChange={(val) => password = val.target.value}
                    />
                </div>
            </div>
            
            <div className="login-and-signup-button-container">
                <button className="login-and-signup-button"
                        onClick={() => RequestLoginAndSignUp(isLoginOption, setIsSignedIn, navigate, username, password, email)}
                >
                    {isLoginOption ? "Log In" : "Sign Up"}
                </button>
            </div>
        </div>
    )
}

async function RequestLoginAndSignUp(isLogIn, setIsSignedIn, navigate, username, password, email) {
    
    const csrfPath = "http://127.0.0.1:8000/api/csrf/";
    const authenticatePath = "http://127.0.0.1:8000/api/token/";
    let csrfCookie = null;
    
    try {
        const response = await fetch(
            csrfPath,
            {
                method: "GET",
                credentials: "include",
            });
        
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        csrfCookie = GetCookie("X-CSRFToken");
    }
    catch (error) {
        console.error(error.message);
        return;
    }

    if(isLogIn)
    {
        try {
            const response = await fetch(
                authenticatePath,
                {
                    method: "POST",
                    credentials: "include",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfCookie,
                    },
                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                });

            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const result = await response.json();
            console.log(result);

            setIsSignedIn(true);
            navigate("/Dashboard");

        } catch (error) {
            console.error(error.message);
        }
    }
    else
    {
        
    }
}