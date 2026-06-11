import { useState } from 'react'
import './App.css'
import Navbar from '@/components/navbar/Navbar.jsx'
import {Outlet} from "react-router";

function App() {

  return (
    <>
        <div className="background-color">
            <Navbar />
            <Outlet />
        </div>
    </>
  )
}

export default App
