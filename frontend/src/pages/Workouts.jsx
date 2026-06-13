import '@/pages/Workouts.css'
import WorkoutNode from "@/components/nodes/WorkoutNode.jsx";

export default function Workouts() {
    return (
        <>
            <div className="container">
                <WorkoutNode exerciseTitle="Core" estimatedTime="15" calories="100" exerciseCount="5" link="/Workouts/Core"/>
                <WorkoutNode exerciseTitle="Arms" estimatedTime="10" calories="50" exerciseCount="3"/>
                <WorkoutNode exerciseTitle="Legs" estimatedTime="10" calories="50" exerciseCount="3"/>
                <WorkoutNode exerciseTitle="Chest" estimatedTime="10" calories="50" exerciseCount="3"/>
                <WorkoutNode exerciseTitle="Back" estimatedTime="10" calories="50" exerciseCount="3"/>
                <WorkoutNode exerciseTitle="full body" estimatedTime="10" calories="50" exerciseCount="3"/>
            </div>
        </>
    )
}