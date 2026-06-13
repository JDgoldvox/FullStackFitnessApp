import "@/pages/Community.css"

export default function Community()
{
    return (
        <>
            <h1 className="community-title"> community page </h1>
            
            <div className="community-main-img-container">
                <img className= "community-main-img" src="../../public/community.jpg" alt="community"/>
            </div>
            
            <section className="community-text-section">
                Welcome to the FitWiz Community—a space designed for everyone, 
                from beginners taking their first steps to seasoned athletes pushing their limits. 
                We believe that fitness is better together, and this hub is where you can turn your 
                individual progress into a shared journey. Whether you are looking for motivation,
                accountability, or a friendly place to discuss your wins, you are in the right spot.
            </section>

            <section className="community-text-section">
                Here, the focus is on connection and growth. You can browse through shared 
                workout plans to spark new ideas for your training, or celebrate your latest 
                personal records alongside others who truly understand the effort behind them. 
                By sharing your journey and seeing the milestones of your peers, you’ll find that 
                the motivation to hit your daily goals—whether that’s hitting your step count, crushing 
                a new lifting personal best, or staying consistent with your nutrition—becomes much easier 
                when you’re part of a team.
            </section>

            <section className="community-text-section">
                How are you planning to structure these community sections—should we highlight recent 
                personal records or feature shared workout plans first?
            </section>
        </>
    )
}
