import { useEffect, useState } from 'react';
import LoginBox from '@/components/Login/LoginAndSignUpNode.jsx'
import '@/pages/Login.css'

export default function Login({ setIsLoggedIn }) {
    
    return (
        <>
            <div className = "center-login">
                <LoginBox setIsSignedIn={setIsLoggedIn} />
            </div>
        </>
    )
}