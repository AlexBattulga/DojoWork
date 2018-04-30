using System;
using System.Collections.Generic;
using System.Linq;

namespace music_linq
{
    class Program
    {
        static void Main(string[] args)
        {
           //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            Artist list = Artists.Where(artist => artist.Hometown == "Mount Vernon").SingleOrDefault();
            Console.WriteLine($"{list.ArtistName}, {list.Age}");


            //Who is the youngest artist in our collection of artists?
            Artist youngest = Artists.Where(age => age.Age == Artists.Min(a => a.Age)).SingleOrDefault();
            Console.WriteLine(youngest.ArtistName);

            //Display all artists with 'William' somewhere in their real name
            List<Artist> foundName = Artists.Where(artist => artist.RealName.Contains("William")).ToList();
            foreach(Artist containsWilliam in foundName)
            {
                Console.WriteLine(containsWilliam.ArtistName);
            }

            //Display the 3 oldest artist from Atlanta
            List<Artist> oldestThree = Artists.Where(home => home.Hometown == "Atlanta").OrderByDescending(a => a.Age).Take(3).ToList();
            foreach(Artist oldest in oldestThree)
            {
                Console.WriteLine(oldest.ArtistName + " --- old");
            }

            //(Optional) Display the Group Name of all groups that have members that are not from New York City
            List<Group> members = Artists.Join(Groups, artist=> artist.GroupId, groups => groups.Id, (artist, groups) => {artist.Group = groups; return artist;})
                                .Where(artist => artist.Hometown != "New York City")
                                .Select(artist => artist.Group).ToList();
            foreach(Group names in members)
            {
                Console.WriteLine(names.GroupName);
            }
            
            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
            List<Artist> membersOfWuTang = Groups.Join(Artists, groups=>groups.Id, artist => artist.GroupId, (groups, artist) => {groups.Group = artist; return groups;})
                        .Where(artist => artist.ArtistName.Contain(group => group.GroupName == "Wu-Tang Clan")).ToList();
            foreach(Artist member in membersOfWuTang)
            {
                Console.WriteLine(member.ArtistName);
            }
        }
    }
}
