import '@/components/nodes/NodeTitle.css'

export default function NodeTitle({title, Icon}) {
    return (
        <div className="shape">
            <p className="title-text">
                {title} 
                <Icon className="icon-style" 
                    size={32}
                /> 
            </p> 
        </div>
    )
}