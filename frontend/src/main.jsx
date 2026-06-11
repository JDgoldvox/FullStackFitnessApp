import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router";
import './index.css'
import App from './App.jsx'
import Dashboard from "@/pages/Dashboard.jsx";
import Goals from "@/pages/Goals.jsx";
import Community from "@/pages/Community.jsx";
import Workouts from "@/pages/Workouts.jsx";
import Core from "@/pages/Workouts/core.jsx";

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
                path: "Workouts",
                Component: Workouts,
            },
            {
                path: "Goals",
                Component: Goals,
            },
            {
                path: "Community",
                Component: Community,
            },
            { // workout routes
                path: "Workouts/Core",
                Component: Core,
            },
        ]
    },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
      <RouterProvider router={router} />
  </StrictMode>,
)
