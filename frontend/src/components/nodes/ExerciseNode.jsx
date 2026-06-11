import '@/components/nodes/ExerciseNode.css'

export default function ExerciseNode({exerciseTitle, reps, sets}) {
    return (
        <>
            <div className="exercise-node-shape">
                <p> {exerciseTitle} </p>
            </div>
        </>
    )
}