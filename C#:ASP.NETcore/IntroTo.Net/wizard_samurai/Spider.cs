namespace wizard_samurai
{
    public class Spider: Enemy
    {
        public Spider(string n): base(n)
        {
            name = n;
            health = 120;
            strength = 35;
        }
        public void Stab(Human obj)
        {
            health += 25;
            attack(obj);
        }
    }
}