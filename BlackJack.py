
# coding: utf-8

# In[48]:

from random import shuffle


# In[49]:

def shuffle_deck():
    deck = range(2,11) * 4
    deck = deck + ['J', 'Q', 'K', 'A']*4
    shuffle(deck)
    return deck


# In[79]:

class BlackJack :
    def __init__(self, deck) :
        self.deck = deck
        self.dealer = []
        self.player = []
        self.win = False
        self.d_stand = False
        self.p_stand = False

    def deal_p(self) :
        card = self.deck.pop()
        print('The card is {}'.format(card))
        self.player.append(card)
        return
    
    def deal_d(self) :
        self.dealer.append(self.deck.pop())
        return
    
    def count(self, hand) :
        As = 0
        n = 0
        for card in hand:
            if card == 'A' :
                As += 1
            elif card == 'J' or card == 'Q' or card == 'K' :
                n += 10
            else :
                n += card
        return As, n
    
    def dealer_play(self):
        As, n = self.count(self.dealer) 
        if n >= 17 or n + As > 17:
            self.d_stand = True
            return
        self.deal_d()
        
    
    def player_play(self, re) :
        if re == 'Hit' :
            self.deal_p()
        if re == 'Stand' :
            self.p_stand = True
        return
    
    def play(self) :
        def get_score(As, n) :
            score = n + As
            for i in range(As) :
                if score + 10 > 21:
                    break
                score += 10
            return score
        def display() :
            print('The dealer\'s cards are ' + ','.join([str(x) for x in self.dealer]) + '.')
        
        # deal the cards
        self.deal_p()
        self.deal_d()
        self.deal_p()
        self.deal_d()
        print('The dealer\'s second card is {}'.format(self.dealer[1]))
        
        # win the game if the player hits 21 and the dealer is not 21
        p_As, p_n = self.count(self.player)
        d_As, d_n = self.count(self.dealer)
        if p_As == 1 and p_n == 10:
            if d_As != 1 or d_n != 10:
                self.win = True
                return
        
        while not self.d_stand or not self.p_stand :
            if not self.p_stand :
                print('Your cards are '+ ','.join([str(x) for x in self.player]) + '.')
                p_As, p_n = self.count(self.player)
                print('Your score is {}'.format(get_score(p_As, p_n)))
                rep = raw_input('Please type \'Hit\' to hit and \'Stand\' to stand ->')
                self.player_play(rep)
                p_As, p_n = self.count(self.player)
                # bust
                if p_As + p_n > 21 :
                    self.win = False
                    display()
                    return 
            
            if not self.d_stand :
                self.dealer_play()
                d_As, d_n = self.count(self.dealer)
                # dealer bust
                if d_As + d_n > 21 :
                    self.win = True
                    display()
                    return
        p_As, p_n = self.count(self.player)
        p_score = get_score(p_As, p_n)
        d_As, d_n = self.count(self.dealer)
        d_score = get_score(d_As, d_n)
        self.win = p_score > d_score
        display()
        return
        


# In[80]:

def main() :
    ans = raw_input("Ready to start ? (Y/N) ->")
    if ans == 'Y':
        num = 0
        win = 0
        deck = []
        while ans == 'Y' :
            if num % 6 == 0:
                deck = shuffle_deck()
            x = BlackJack(deck)
            x.play()
            if x.win :
                print('You win !')
                win += 1
            else :
                print('You lose !')
            num += 1
            win_percent = win * 1.0 / num
            print ('Win percentage is {}'.format(win_percent))
            ans = raw_input("Continue ? (Y/N) ->")
                


# In[81]:

if __name__ == '__main__': main()

