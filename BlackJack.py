
# coding: utf-8

# In[19]:

from random import shuffle


# In[20]:

def shuffle_deck():
    deck = range(2,11) * 4
    deck = deck + ['J', 'Q', 'K', 'A']*4
    shuffle(deck)
    return deck


# In[26]:

class BlackJack :
    def __init__(self, deck) :
        self.deck = deck
        self.dealer = []
        self.player = []
        self.win = False
        self.flag = True

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
            self.flag = False
            return
        self.deal_d()
        
    
    def player_play(self, re) :
        if re == 'Hit' :
            self.deal_p()
        if re == 'Stand' :
            return
    
    def play(self) :
        def get_score(As, n) :
            score = n + As
            for i in range(As) :
                if score + 10 > 21:
                    break
                score += 10
            return score
            
        self.deal_p()
        self.deal_d()
        print('The dealer\'s card is {}'.format(self.dealer[0]))
        self.deal_p()
        self.deal_d()
        p_As, p_n = self.count(self.player)
        d_As, d_n = self.count(self.dealer)
        if p_As == 1 and p_n == 10:
            if d_As != 1 or d_n != 10:
                self.win = True
                return
        
        while True :
            re = raw_input('Please type \'Hit\' to hit and \'Stand\' to stand ->')
            if (self.flag is False) and (re == 'Stand') :
                break
            
            self.player_play(re)
            p_As, p_n = self.count(self.player)
            # bust
            if p_As + p_n > 21 :
                self.win = False
                return
            
            if self.flag :
                self.dealer_play()
                d_As, d_n = self.count(self.dealer)
                if d_As + d_n > 21 :
                    self.win = True
                    return 
        
        p_As, p_n = self.count(self.player)
        p_score = get_score(p_As, p_n)
        d_As, d_n = self.count(self.dealer)
        d_score = get_score(d_As, d_n)
        self.win = p_score > d_score
        return
        


# In[ ]:

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
                


# In[ ]:

if __name__ == '__main__': main()

