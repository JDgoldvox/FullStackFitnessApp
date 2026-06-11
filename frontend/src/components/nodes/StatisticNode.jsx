import '@/components/nodes/StatisticNode.css'
import NodeTitle from "@/components/nodes/NodeTitle.jsx"

export default function StatisticNode({title, Icon, statistic, unit, goal, fact}) {
    return (
        <>
            <div className="small-node">
                    <NodeTitle title={title} Icon={Icon}/>  
                    
                    <p className="node-statistic">
                        {statistic} 
                        <span style={{ fontWeight: "normal"}}>  {unit}</span>
                    </p>
                    <p className="node-goal">
                        <span style={{ fontWeight: "normal"}}> {goal} {unit} to go!</span>
                    </p>
                    <p className="node-fact">
                        {fact}
                    </p>
            </div>
        </>
    )
}
