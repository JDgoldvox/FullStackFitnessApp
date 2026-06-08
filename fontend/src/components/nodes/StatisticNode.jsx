import '@/Components/StatisticNode.css'

export default function SmallStatisticNode({statistic}) {
    return (
        <>
            <div className="small-node">
                
                
                <p className="node-value">{statistic}</p>
            </div>
        </>
    )
}

export function LargeStatisticNode()
{
    
}