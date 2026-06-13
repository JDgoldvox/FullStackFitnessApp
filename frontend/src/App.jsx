import { useState } from 'react'
import './App.css'
import Navbar from '@/components/navbar/Navbar.jsx'
import {Outlet} from "react-router";

function App() {

  return (
    <>
        <title> FitWiz </title>
        <div className="background-color">
            <link rel="icon" href="/favicon.ico" />
            <Navbar />
            <Outlet />
        </div>
    </>
  )
}

export default App
