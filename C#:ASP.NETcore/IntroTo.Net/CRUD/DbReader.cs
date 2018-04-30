using System;
using System.Collections.Generic;

namespace CRUD 
{
    public static class DbReader
    {
        public static void Read()
        {
            List<Dictionary <string, object>> users = DbConnector.Query("SELECT * FROM users");
            foreach(var user in users)
            {
                Console.WriteLine($"First Name: {user["FirstName"]}");
                Console.WriteLine($"Last Name: {user["LastName"]}");
                Console.WriteLine($"Favorite Number: {user["FavoriteNumber"]}");
                Console.WriteLine($"Date Created: {user["created_at"]}");
                System.Console.WriteLine("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
            }
        }
        public static User PromptForUser()
        {
            Console.WriteLine("Enter a First Name: ");
            string first = Console.ReadLine();
            Console.WriteLine("Enter a Last Name: ");
            string last = Console.ReadLine();
            Console.WriteLine("Enter a Favorite Number: ");
            string num = Console.ReadLine();
            return new User()
            {
                FirstName = first,
                LastName = last,
                FavoriteNumber = num
            };
        }
        public static void Update(string userId)
        {
            User userToUpdate = PromptForUser();
            string query = 
            $@"
                UPDATE users SET FirstName = '{userToUpdate.FirstName}', 
                LastName = '{userToUpdate.LastName}', 
                FavoriteNumber = '{userToUpdate.FavoriteNumber}' 
                WHERE id = {userId}
            ";
            DbConnector.Execute(query);
        }
        // public static void Delete(int userId)
        // {
        //     string query = 
        //     $@"
        //         DELETE FROM users WHERE id = {userId}
        //     ";
        //     DbConnector.Execute(query);
        // }                                            
    }
}