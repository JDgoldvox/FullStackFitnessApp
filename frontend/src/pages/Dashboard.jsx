import SmallStatisticNode from "@/components/nodes/StatisticNode.jsx";
import '@/pages/Dashboard.css';

export default function Dashboard() {
    return (
        <>
            <div className="title">
                <p> 
                    Hello { }
                    <b>Liam</b>
                    , Welcome back to the dashboard.
                </p>
            </div>
            
            
            <div className="grid-container">
                {/* 1. Water */}
                <SmallStatisticNode
                    title="water"
                    statistic="3789"
                    unit="ml"
                    goal="5000"
                    fact="15 glasses drank"
                />

                {/* 2. Calories */}
                <SmallStatisticNode
                    title="calories"
                    statistic="1850"
                    unit="kcal"
                    goal="2200"
                    fact="Remaining: 350 kcal"
                />

                {/* 3. Steps */}
                <SmallStatisticNode
                    title="steps"
                    statistic="8,432"
                    unit="steps"
                    goal="10,000"
                    fact="Distance: 5.8"
                />

                {/* 4. Exercises Completed */}
                <SmallStatisticNode
                    title="exercises"
                    statistic="3"
                    unit="exercises"
                    goal="5 weekly"
                    fact="Total Time: 1h 15m"
                />

                {/* 5. Heartrate */}
                <SmallStatisticNode
                    title="heartrate"
                    statistic="72"
                    unit="bpm"
                    goal="Resting Avg: 64"
                    fact="Status: Normal"
                />
            </div>
        </>
    )
}

function example()
{
    
}