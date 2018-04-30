using System;

namespace Csharp_fundamentals
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1) Create a loop that prints all values from 1-255
            // int start = 1;
            // int end = 255;
            // for(int i = start; i <= end; i++){
            //     Console.WriteLine(i);
            // }
            // 2) Create a new loop that prints all values from 1-100 that are divisible by 3 or 5, but not both
            // int start = 1;
            // int end = 100;
            // for(int i = start; i <= end; i++){
            //     if(i % 3 == 0 && i % 5 == 0){
            //         continue;
            //     }else if(i % 5 == 0 && i % 3 != 0){
            //         Console.WriteLine(i);
            //     }else if (i % 5 != 0 && i % 3 == 0){
            //         Console.WriteLine(i);
            //     }
            // }
            // 3) Modify the previous loop to print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for numbers that are multiples of both 3 and 5
            // int start = 1;
            // int end = 100;
            // for(int i = start; i <= end; i++){
            //     if(i % 3 == 0 && i % 5 == 0){
            //         Console.WriteLine("FizzBuzz");
            //     }else if(i % 5 == 0 && i % 3 != 0){
            //         Console.WriteLine("Buzz");
            //     }else if (i % 5 != 0 && i % 3 == 0){
            //         Console.WriteLine("Fizz");
            //     }else{
            //         Console.WriteLine(i);
            //     }
            // }
            // 4) If you used modules in the last step, try doing the same without using it. Vice-versa for those who didn't!
            // int start = 1;
            // int end = 30;
            // for(int i = start; i <= end; i++){
            //     if(i == 15 || i == 30){
            //         Console.WriteLine("FizzBuzz");
            //     }else if(i == 5 || i == 10 || i == 15 || i == 20 || i == 25 || i  == 30){
            //         Console.WriteLine("Buzz");
            //     }else if (i == 3 || i == 6 || i == 9 || i == 12 || i == 15 || i == 18 || i == 21 || i == 24 || i == 27 || i == 30){
            //         Console.WriteLine("Fizz");
            //     }else{
            //         Console.WriteLine(i);
            //     }
            // }
            // 5) Generate 10 random values and output the respective word, in relation to step three, for the generated values
            int start = 1;
            int end = 10;
            int rand_num = 0;
            Random rand = new Random();
            for(int i = start; i <= end; i++){
                rand_num = rand.Next(1, 100);
                if(rand_num % 3 == 0 && rand_num % 5 == 0){
                    Console.WriteLine("FizzBuzz"+rand_num);
                }else if(rand_num % 3 == 0 && rand_num % 5 != 0){
                    Console.WriteLine("Fizz");
                }else if(rand_num % 5 == 0 && rand_num % 3 != 0){
                    Console.WriteLine("Buzz");
                }else{
                    Console.WriteLine(rand_num);
                }
            }
        }
    }
}
