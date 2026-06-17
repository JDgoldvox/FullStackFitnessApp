import '@/pages/Goals.css'

export default function Goals() {
    return (
        <>
            <h1 className= "goals-title"> Goals </h1>
            
            <section className="goals-container">
                <h2> Water </h2>
                
                <div className="goal-settings">
                    <input type="number" placeholder="1000"/> <p> ml </p>
                </div>
            </section>

            <section className="goals-container">
                <h2> Food </h2>
                <ul className="goal-settings">
                    <li>
                        <p> Calories: </p> 
                        <input type="number" placeholder="1000"/>
                        <p> Kcal </p>
                    </li>
                    <li>
                        <p> Protein: </p> 
                        <input type="number" placeholder="1000"/> 
                        <p> g </p>
                    </li>
                    <li>
                        <p> Carbs: </p>
                        <input type="number" placeholder="1000"/> 
                        <p> g </p>
                    </li>
                </ul>
            </section>

            <section className="goals-container">
                <h2> Steps </h2>
                <div className="goal-settings">
                    <input type="number" placeholder="1000"/> 
                    <p> Steps </p>
                </div>
            </section>

            <section className="goals-container">
                <h2> Exercises </h2>
                <div className="goal-settings">
                    <input type="number" placeholder="5"/>
                    <p> Count </p>
                </div>
            </section>

            <section className="goals-container">
                <h2> Heartrate </h2>
                <div className="goal-settings">
                    <input type="number" placeholder="1000"/>
                    <p> Bpm </p>
                </div>
            </section>
            
            <br></br>
        </>
    )
}