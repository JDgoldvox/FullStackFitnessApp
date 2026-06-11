import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router";
import './index.css'
import App from './App.jsx'
import Dashboard from "@/pages/Dashboard.jsx";
import Exercises from "@/pages/Exercises.jsx";
import Goals from "@/pages/Goals.jsx";
import Community from "@/pages/Community.jsx";

const router = createBrowserRouter([
    { 
        path: "/",
        Component: App,
        children: [
            {
                index: true,
                Component: Dashboard,
            },
            {
                path: "Exercises",
                Component: Exercises,
            },
            {
                path: "Goals",
                Component: Goals,
            },
            {
                path: "Community",
                Component: Community,
            }
        ]
    },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
      <RouterProvider router={router} />
  </StrictMode>,
)
