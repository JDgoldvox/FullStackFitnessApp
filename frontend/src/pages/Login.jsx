import { useEffect, useState } from 'react';
import LoginBox from '@/components/Login/LoginAndSignUpNode.jsx'
import '@/pages/Login.css'

export default function Login() {
    const [isSignUp, setIsSignUp] = useState(false);
    
    return (
        <>
            <div className = "center-login">
                <LoginBox />
            </div>
        </>
    )
}

//const [data, setData] = useState(null);

// useEffect(() =>
// {
//     async function GetData() {
//         const url = "https://isitdownstatus.com/api/v1/status/discord";
//         try {
//             const response = await fetch(url);
//             if (!response.ok) {
//                 throw new Error(`Response status: ${response.status}`);
//             }
//
//             const result = await response.json();
//             setData(result);
//         } catch (error) {
//             console.error(error.message);
//         }
//     }
//
//     GetData();
// } ,[]);
//
// return (
//     <>
//         <p> login </p>
//         <p>{data?.data?.slug ?? "Loading..."}</p>
//     </>
// )