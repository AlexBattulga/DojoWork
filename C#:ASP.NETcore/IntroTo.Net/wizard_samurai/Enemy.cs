using System;
using System.Collections.Generic;

namespace wizard_samurai
{
    public class Enemy
    {
        public string name;

    //The { get; set; } format creates accessor methods for the field specified
    //This is done to allow flexibility
    public int health { get; set; }
    public int strength { get; set; }
    public int intelligence { get; set; }
    public int dexterity { get; set; }

    public Enemy(string person)
    {
        name = person;
        strength = 3;
        intelligence = 3;
        dexterity = 3;
        health = 100;
    }
    public Enemy(string person, int str, int intel, int dex, int hp)
    {
        name = person;
        strength = str;
        intelligence = intel;
        dexterity = dex;
        health = hp;
    }
    public void attack(Human obj)
    {
        if(obj == null)
        {
            Console.WriteLine("Failed Attack");
        }
        else
        {
            obj.health -= strength * 5;
        }
    }
    }
}