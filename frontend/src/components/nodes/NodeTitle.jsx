import '@/components/nodes/NodeTitle.css'
import { Smile } from "lucide-react";

export default function NodeTitle({title}) {
    return (
        <div className="shape">
            <p className="title-text">
                {title}
                <Smile style={{ marginLeft: '12px' }} /> 
            </p> 
        </div>
    )
}