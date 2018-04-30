namespace wizard_samurai
{
    public class Zombie: Enemy
    {
        public Zombie(string n): base(n)
        {
            name = n;
            health = 100;
            strength = 30;
        }
        public void Bite(Human obj)
        {
            health += 25;
            attack(obj);
        }
    }
}