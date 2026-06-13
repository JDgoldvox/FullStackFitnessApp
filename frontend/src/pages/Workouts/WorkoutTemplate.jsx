import '@/pages/Workouts/WorkoutTemplate.css'
import WorkoutNode from "@/components/nodes/ExerciseNode.jsx"

export default function WorkoutTemplate({
                                            workoutName, 
                                            description, 
                                            exerciseCount, 
                                            estimatedTime, 
                                            calories, 
})
{
    return (
        <>
            <div className="workout-banner">
                <img
                    src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/66/93/04/caption.jpg?w=800&h=800&s=1"
                    alt="placeholder"
                />
                <h1> {workoutName} </h1>
            </div>
            
            <div className="info-box"> 
                <p>{description}</p> 
            </div>

            <ul className="workout-list">
                <li> <WorkoutNode exerciseTitle="Situps" sets={5} reps={10}/> </li>
                <li> <WorkoutNode exerciseTitle="Plank" sets={3} reps={1}/> </li>
                <li> <WorkoutNode exerciseTitle="Russian Twists" sets={4} reps={20}/> </li>
                <li> <WorkoutNode exerciseTitle="Leg Raises" sets={4} reps={12}/> </li>
                <li> <WorkoutNode exerciseTitle="Mountain Climbers" sets={3} reps={30}/> </li>
                <li> <WorkoutNode exerciseTitle="Bicycle Crunches" sets={4} reps={15}/> </li>
            </ul>
        </>
    )
}