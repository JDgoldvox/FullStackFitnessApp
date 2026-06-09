import '@/components/navbar/Navbar.css'
import {NavLink} from 'react-router'

export default function Navbar() {
    return (
        <>
            <nav>
                
                <div className="navbar-logo">
                    <NavLink to="/">FitWiz</NavLink>
                </div>
                
                <ul className="nav-bar">
                    <li className="nav-bar-item">
                        <NavLink to="/">Dashboard</NavLink>
                    </li>
                    <li className="nav-bar-item">
                        <NavLink to="/Exercises">Exercises</NavLink>
                    </li>
                    <li className="nav-bar-item">
                        <NavLink to="/Goals">Goals</NavLink>
                    </li>
                    <li className="nav-bar-item">
                        <NavLink to="/Community">Community</NavLink>
                    </li>
                </ul>
            </nav>
        </>
    )
}