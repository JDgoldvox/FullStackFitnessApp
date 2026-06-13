import WorkoutTemplate from "@/pages/Workouts/WorkoutTemplate.jsx"

export default function Core()
{
    let description = "Build a rock-solid foundation with this targeted, high-intensity session designed to challenge your deep abdominals, obliques, and lower back. By combining stabilizing holds with dynamic movements, this workout improves your posture, increases functional power, and enhances rotational stability, acting as the perfect \"fire-starter\" to strengthen your center and improve your balance.";
    
    return (
        <>
            <WorkoutTemplate 
                workoutName="core" 
                calories={100} 
                exerciseCount={5} 
                estimatedTime={15}
                description={description}/>
        </>
    )
}