import '@/components/navbar/Navbar.css'
import {NavLink} from 'react-router'

export default function Navbar() {
    return (
        <>
            <nav className="navbar-container">
                
                <div className="navbar-logo">
                    <NavLink to="/">FitWiz</NavLink>
                </div>
                
                <ul className="navbar-links">
                    <li className="navbar-item">
                        <NavLink to="/">Dashboard</NavLink>
                    </li>
                    <li className="navbar-item">
                        <NavLink to="/Exercises">Exercises</NavLink>
                    </li>
                    <li className="navbar-item">
                        <NavLink to="/Goals">Goals</NavLink>
                    </li>
                    <li className="navbar-item">
                        <NavLink to="/Community">Community</NavLink>
                    </li>
                </ul>
            </nav>
        </>
    )
}