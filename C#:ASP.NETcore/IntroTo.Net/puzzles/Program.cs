using System;
using System.Collections.Generic;

namespace puzzles
{
    class Program
    {
        static void Main(string[] args)
        {
            // int []randArr = RandomArray();
            //     Console.WriteLine($"Max value is: {randArr[0]}");
            //     Console.WriteLine($"Min value is: {randArr[1]}");
            //     Console.WriteLine($"Total sum value: {randArr[2]}");

            // Console.WriteLine(TossCoin());
            // double ratio = TossMultipleCoins(2);
            // Console.WriteLine(ratio);
            List<string> name = Names();
            Console.Write("\nNames longer than 5 characters: ");
            foreach(string list in name)
            {
                Console.Write(list+", ");
            }
            Console.Write("\n");
        }
        static int[] RandomArray()
        {
            // 1. Random array
            List<int> val = new List<int>();
            int max = Int32.MinValue;
            int min = Int32.MaxValue;
            int sum = 0;
            Random rand = new Random();
            for(int i=0; i<10; i++)
            {
                val.Add(rand.Next(5, 25));    // Adding a 10 random values to an array
            }
            for(int i=0; i<val.Count; i++)
            {
                if(val[i]>max)              // Looking for max value from the array
                {
                    max=val[i];             // Assigning a max value to var max
                }
                else if(val[i] < min)
                {
                    min=val[i];
                }
                sum += val[i];              // Adding up all values of the array
            }
            int[] newArray = new int[]{max, min, sum};
            return newArray;
        }
        // 2. Coin Flip
        static string TossCoin()
        {
            Console.WriteLine(".::::::::::::: Tossing a Coin :::::::::::::::.");
            string HeadsOrTails = "";
            Random rand = new Random();
            int coin = rand.Next(0, 2);
            if(coin == 1 )
            {
                HeadsOrTails += "Heads";
            }
            else
            {
                HeadsOrTails +="Tails";
            }
            return HeadsOrTails;
        }
        static double TossMultipleCoins(int num)
        {
            string toss = "";
            double count = 0;
            for(int i=1; i<=num; i++)
            {
               toss = TossCoin();
               if(toss == "Heads")
               {
                   count++;
               }
            }
            return count/num;
        }
        // 3. Names
        static List<string> Names()
        {
            string[] arr = new string[]{"Todd", "Tiffany", "Charlie", "Geneva", "Sydney"};
            Array.Sort(arr);
            List<string> newList = new List<string>();
            Console.Write("Names are in new order :");
            foreach(string names in arr)
            {
                Console.Write(names+", ");
                if(names.Length>5)
                {
                    newList.Add(names);
                }
            }
            return newList;
        }
    }
}
