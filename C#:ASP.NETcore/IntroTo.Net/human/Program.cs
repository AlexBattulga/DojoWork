using System;

namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human human = new Human("Alex");
            Human obj = new Human("Alex", 90, 90, 80, 100);
            Console.WriteLine(obj.health);
            obj.attack();
            obj.attack();
            obj.attack();
            obj.attack();
        }
    }
}
