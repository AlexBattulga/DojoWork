using System;

namespace wizard_samurai 
{
    public class Wizard: Human
    {
        Random rand;
        public Wizard(string n): base(n)
        {
            health = 50;
            intelligence = 25;
        }
        public void heal()
        {
            health += 10 * intelligence;
        }
        public void fireball(object obj)
        {
            Human enemy = obj as Human;
            rand = new Random();
            if(enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }else
            {
                int dmg = rand.Next(20, 50);
                enemy.health -= dmg;
            }
        }
    }
}