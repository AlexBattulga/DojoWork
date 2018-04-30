using System;

namespace wizard_samurai
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Choose your character!"+"\n1. Ninja\t"+"a.Zombie"+"\n2. Wizard\t"+"b. Spider"+"\n3. Samurai");
            string chosen = display();
            Console.WriteLine("Choose what character you want to fight with"+"\n1. Ninja\t"+"a.Zombie"+"\n2. Wizard\t"+"b. Spider"+"\n3. Samurai");
            string enemy = display();
            Console.WriteLine($"You selected the {chosen} agianst to {enemy}. {chosen}'s skills will not disappoint you");
            Console.WriteLine("Lets attack to your enemy");
        }
        static string display()
        {
            Human hero = null;
            Enemy beast = null;
            string chosen = "";
            int count = 0;
            while(hero == null && beast == null)
            {
                string val = Console.ReadLine();
                switch(val)
                {
                    case "1": hero = new Ninja("Hon Gil Don");
                    break;
                    case "2": hero = new Wizard("Butcher");
                    break;
                    case "3": hero = new Samurai("Angry Samurai");
                    break;
                    case "a": beast = new Zombie("Death");
                    break;
                    case "b": beast = new Spider("BroodMother");
                    break;
                    default: Console.WriteLine("No other cases found");
                    break;
                }
                if(hero != null && beast == null)
                {
                    chosen += hero.name;
                }
                else if(hero == null && beast != null)
                {
                    chosen += beast.name;
                }
                count++;
            }
            return chosen;
        }
    }
}