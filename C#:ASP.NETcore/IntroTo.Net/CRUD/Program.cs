using System;

namespace CRUD
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Type a user id to update:");
            string userId = Console.ReadLine();
            DbReader.Update(userId);
            DbReader.Read();
            // Console.WriteLine("Type a user id to delete:");
            // int deleteUser = Console.Read();
            // DbReader.Delete(deleteUser);
            // Console.WriteLine("Thank you!");
        }
    }
}