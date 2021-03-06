namespace deck_of_cards
{
     public class Card{
         private int _suit;
         private int _val;
         static string[] suits = {"Spades", "Clubs", "Diamonds", "Hearts"};
         public string Suit
         {
             get{ return suits[_suit];}
         }
         public string Value
         {
             get
             {
                 switch(_val)
                 {
                     case 1: 
                        return "Ace";
                     case 11:
                        return "Jack";
                     case 12:
                        return "Queen";
                     case 13:
                        return "King";
                     default:
                        return _val.ToString();
                 }
             }
         }
         public Card(int val, int suit)
         {
             _suit = suit;
             _val = val;
         }
         public override string ToString()
         {
            return Suit + " of " + Value;
         }
     }
}