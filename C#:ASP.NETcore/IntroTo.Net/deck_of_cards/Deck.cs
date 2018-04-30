using System;
using System.Collections.Generic;

namespace deck_of_cards
{
     public class Deck {
        private List<Card> cards;

        public Deck() 
        {
            cards = new List<Card>();
            for(int i=0; i<=3; i++)
            {
                for(int j=0; j<=13; j++)
                {
                    Card card = new Card(j, i);
                    cards.Add(card);
                }
            }
        }
        public Card Deal(int a) {
            if(cards.Count > 0) {
                Card temp = cards[a];
                cards.RemoveAt(a);
                return temp;
            }
            return null;
        }

        public Deck Shuffle() {
            Random rand = new Random();
            for(int idx = cards.Count - 1; idx >= 0; idx--) {
                int randIdx = rand.Next(idx);
                Card temp = cards[randIdx];
                cards[randIdx] = cards[idx]; 
                cards[idx] = temp;
            }
            return this;
        }

        public override string ToString() {
            string info = "";
            foreach(Card card in cards) {
                info += card + "\n";
            }
            return info;
        }
    }
}