using System;
using System.Collections.Generic;
namespace collections_practice
{
    class Program
    {
        static void Main(string[] args)
        {   
            // three basic arrays
            int [] integers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            string [] names = {"Tim", "Martin", "Nikki", "Sara"};
            bool [] alternate = new bool[10];
            // Multiplication table
            // int [,] arr = new int [11, 11];
            // for(int i = 1; i < 11; i++){
            //     Console.WriteLine("\n");
            //     for(int j = 1; j < 11; j++){
            //         arr[i, j] = i * j;
            //         Console.Write(arr[i, j] + "\t");
            //     }
            // }
            // List of Flavors
            List<string> icecream = new List<string>();
            icecream.Add("Rocky Road");
            icecream.Add("Strawberry");
            icecream.Add("Chocolate");
            icecream.Add("Caramel cone");
            icecream.Add("Belginan Chocolate");
            icecream.Add("Dulce de leche");
            Console.WriteLine("Number of items in List<icecream> is: " + icecream.Count);
            Console.WriteLine("Third item of the List: " + icecream[2]);
            icecream.Remove("Chocolate");
            Console.WriteLine("New length of the List is now: " + icecream.Count);
            //User info Dictionary
            Random random = new Random();
            Dictionary<string,string> profile = new Dictionary<string,string>();
            foreach(string name in names)
            {
                profile[name] = icecream[random.Next(icecream.Count)];
            }
            foreach(var user in profile)
            {
                Console.WriteLine(user);
            }
        }
    }
}
