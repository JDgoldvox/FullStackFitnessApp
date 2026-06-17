import '@/components/Login/LoginAndSignUpNode.css'
import { useState } from 'react';
import {Mail, KeyRound, User} from 'lucide-react'

export default function LoginAndSignUpNode(setIsSignedIn) {
    
    const [isLogIn, setIsLogIn] = useState(true);
    
    let password = "";
    let email = "";
    let username = "";
    
    return (
        <div className="login-and-signup-node">
            <div className = "login-and-signup-options">
              <button 
                  className={isLogIn ? "login-button-active" : "login-button-inactive"}
                  onClick={() => setIsLogIn(true)}
              >
                  Login
              </button>
              <button 
                  className={isLogIn ? "signup-button-inactive" : "signup-button-active"}
                  onClick={() => setIsLogIn(false)}
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
                    isLogIn ? null : 
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
                        onClick={() => RequestLoginAndSignUp(isLogIn, username, password, email)}
                >
                    {isLogIn ? "Log In" : "Sign Up"}
                </button>
            </div>
        </div>
    )
}

function RequestLoginAndSignUp(isLogIn, username, password, email)
{
    alert(`${username} ${password} ${email}`);
    
    //isSignedIn
    
    
    if(isLogIn) //logging in
    {
        
    }
}