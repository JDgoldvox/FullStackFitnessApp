import '@/components/nodes/ExerciseNode.css'

export default function ExerciseNode({exerciseTitle, reps, sets}) {
    
    function handleCheckboxChange() {
        alert("Checkbox changed!");
    }
    
    return (
        <>
            <div className="exercise-node-shape">
                <p> {reps} x {exerciseTitle} for {sets} sets</p>
                <input type={"checkbox"} onChange={handleCheckboxChange}/>
            </div>
        </>
    )
}