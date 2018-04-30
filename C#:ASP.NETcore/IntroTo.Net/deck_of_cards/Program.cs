using System;

namespace deck_of_cards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck myDeck = new Deck();
            Player tester = new Player("ALex");
            
            Console.WriteLine(myDeck.Deal(5)+ "Deleted");
            Console.WriteLine(myDeck);
        }
    }
}
