namespace wizard_samurai
{
    public class Samurai : Human
    {
        public Samurai(string n) : base(n)
        {
            health = 200;
        }
        public void death_blow(Enemy obj)
        {
            if(obj != null)
            {
                attack(obj);
                if(obj.health < 50)
                {
                    obj.health = 0;
                }
            }
        }
        public void meditate()
        {
            health = 200;
        }
    }
}