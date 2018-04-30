namespace wizard_samurai
{
    public class Ninja : Human
    {
       public Ninja(string n):base(n)
       {
            name = n;
            strength = 30;
            intelligence = 45;
            dexterity = 175;
            health = 100;
       }
        public void Steal(Enemy obj)
        {
            if(obj != null)
            {
                attack(obj);
                health +=10;
            }
        }
        public void Get_Away()
        {
            health -= 15;
        }
    }
}
