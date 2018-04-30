using System;
using System.Collections.Generic;
namespace basic_13
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr1 = {-10, 5, -30, 7};
            int[] arr2 = {20, 5, 30, 9};
            // solution1();
            // solution2();
            // solution3();
            // solution4();
            // solution5(arr1);
            // solution6(arr1);
            // solution7();
            // solutuion8(arr1);
            // solution9(arr2);
            // solution10(arr1);
            // solution11(arr2);
            // solution12(arr2);
            solution13(arr1);
        }
         // 1. Print 1 - 255
        static void solution1(){
            for(int i = 1; i <= 255; i++)
        {
            Console.WriteLine(i);
        }
        }
        // 2.Print odd numbers between 1-255
        static void solution2()
        {
            for(int i = 1; i <= 255; i++)
            {
                if(i % 2 != 0)
                {
                    Console.WriteLine("Odd numbers: " + i);
                }
            }
        }
        // 3. Print sum
        static void solution3()
        {
            int sum = 0;
            for(int i = 0; i <= 255; i++)
            {
                sum = sum + i;
                Console.WriteLine("New number: " + i + " Sum: " + sum);
            }
        }
        // 4. Iterating through an Array
        static void solution4()
        {
            int [] array = {1, 3, 5, 7, 9, 13};
            for(int i = 0; i < array.Length; i++)
            {
                Console.WriteLine(array[i]);
            }
        }
        // 5. Find max
        static void solution5(int[]arr)
        {
            int max = int.MinValue;
            for(int i=0; i<arr.Length; i++)
            {
                if(arr[i] > max)
                {
                    max=arr[i];
                }
            }
            Console.WriteLine($"Max value is {max}");
        }
        // 6. Get Average
        static void solution6(int[]arr)
        {
            int sum = 0;
            int avg = 0;
            int count = 0;
            foreach(int array in arr)
            {
                sum += array;
                count++;
            }
            avg = sum / count;
            Console.WriteLine($"Average value is {avg}");
        }
        // 7. Array with odd numbers
        static void solution7()
        {
            List<int> list = new List<int>();
            for(int i = 1; i <= 255; i++)
            {
                if(i % 2 != 0)
                {
                    list.Add(i);
                }
            }
            string brackets = "[";
            foreach(int li in list)
            {
                brackets += li + " ";
            }
            brackets += "]";
            Console.WriteLine(brackets);
        }
        // 8. Greater than Y
        static void solutuion8(int[] arr)
        {
            int y = 5;
            int count = 0;
            foreach(int array in arr)
            {
                if(array > y)
                {
                    count++;
                }
            }
            Console.WriteLine($"There are {count} values greater than Y");
        }
        // 9. Square the Values
        static void solution9(int []arr)
        {
            string newArray = "[ ";
            foreach(int array in arr)
            {
                newArray += array*array + " ";
            }
            newArray +="]";
            Console.WriteLine(newArray);
        }
        // 10. Eliminate Negative numbers
        static void solution10(int []arr)
        {
            string brackets = "[";
            for(int i = 0; i < arr.Length; i++)
            {
                if(arr[i] < 1)
                {
                    arr[i]=0;
                }
                brackets += arr[i] + " ";
            }
            brackets += "]";
            Console.WriteLine(brackets);
        }
        // 11. Min, Max and Average
        static void solution11(int[] arr)
        {
            int max = Int32.MinValue;
            int min = Int32.MaxValue;
            int avg = 0;
            int sum = 0;
            for(int i = 0; i < arr.Length; i++)
            {
                if(arr[i] > max)
                {
                    max = arr[i];
                }else if (arr[i] < min){
                    min = arr[i];
                }
                sum += arr[i];
            }
            avg = sum/arr.Length;
            Console.WriteLine($"Max number {max}, min number {min} and average {avg}");
        }
        // 12. Shifting values in an array
        static void solution12(int[]arr)
        {
            for(int i=0; i<arr.Length-1; i++)
            {
                    arr[i]=arr[i+1];
            }
            arr[arr.Length-1]=0;
            string brackets = "[";
            foreach(int array in arr)
            {
                brackets += array+" ";
            }
            brackets += "]";
            Console.Write(brackets);
        }
        // 13. Number to String
        static void solution13(int[]arr)
        {
            List<object> newList = new List<object>();
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] < 0)
                {
                    newList.Add("Dojo");
                } 
                else 
                {
                    newList.Add(arr[i]);
                }
            }
            object[] newArray = new object[newList.Count];
            for (int i = 0; i < newList.Count; i++)
            {
                newArray[i] = newList[i];
            }
            string brackets = "[ ";
            foreach(object ar in newArray)
            {
                brackets += ar+ " ";
            }
            brackets += " ]";
            Console.Write(brackets);
        }
    }
}
