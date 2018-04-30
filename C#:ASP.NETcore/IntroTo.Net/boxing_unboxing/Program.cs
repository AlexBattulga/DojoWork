using System;
using System.Collections.Generic;

namespace boxing_unboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Object> obj = new List<Object>();
            obj.Add(7);
            obj.Add(28);
            obj.Add(-1);
            obj.Add(true);
            obj.Add("Chair");
            int add = 0;
            foreach(object val in obj)
            {
                Console.WriteLine(val);
                if(val is int)
                {
                    add = add + (int)val;
                }
            }
            Console.WriteLine("Total value of integers is: " + add);
        }
    }
}
