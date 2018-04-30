using System;

namespace human{
    public class Human{
        public string name;
        public int strength = 3;
        public int intelligence = 3;
        public int dexterity = 3;
        public int health = 100;
        public Human(string n){
            name=n;
        }
        public Human(string n, int s, int i, int d, int h){
            name = n;
            strength = s;
            intelligence = i;
            dexterity = d;
            health = h;
        }
        public void attack(){
            health -= 5*strength;
            Console.WriteLine("Strength is now: {0}", health);
        }
    }
}