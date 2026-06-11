import '@/components/nodes/WorkoutNode.css'
import NodeTitle from "@/components/nodes/NodeTitle.jsx";
import {NavLink} from 'react-router'

export default function WorkoutNode({exerciseTitle, exerciseCount, estimatedTime, calories, link}) 
{
    return (
        <>
            <NavLink className="node-container" to={link}>
                <NodeTitle title={exerciseTitle} />
                
                <div className="row-container">
                    <p className="special-number">{estimatedTime}</p>
                    <p>Minutes</p>
                </div>

                <div className="row-container">
                    <p className="special-number">{exerciseCount}</p>
                    <p>Exercises</p>
                </div>

                <div className="row-container">
                    <p className="special-number">{calories}</p>
                    <p>Calories</p>
                </div>

                <p> Click to start </p>
            </NavLink>
            
        </>
    )
    
}