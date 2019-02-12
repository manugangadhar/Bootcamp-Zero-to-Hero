import random
card_types = ['s', 'h', 'd', 'c']
global players_list
players_list = {}
global dealer_cards
dealer_cards = []
global fiftytwo_cards
fiftytwo_cards = set()

class Blackjack:

    def __init__(self, name, bet, player_cards, gain_loss):

        self.name = name
        self.bet = bet
        self.player_cards = player_cards
        self.gain_loss = gain_loss

    def card_distribute(self, set_of_cards):
        self.player_cards.append(set_of_cards.pop())

    def player_stand(self):
        pass


    def player_hit(self, set_of_cards):
        print(f"*****Player {self.name} will take a hit*****")
        self.player_cards.append(set_of_cards.pop())



    def player_split(self):
        pass

    def calculate_wins(self):
        self.gain_loss = self.gain_loss + self.bet
        return self.gain_loss

    def calculate_loss(self):
        self.gain_loss = self.gain_loss - self.bet
        return self.gain_loss

    def value_of_cards(self, player_cards):
        card_values = []
        for i in player_cards:
            if i[1:] in ['J','Q','K']:
                card_values.append(10)
            elif i[1:] in ['1','2','3','4','5','6','7','8','9','10']:
                card_values.append(int(i[1:]))
            else:
                if (21 - sum(card_values)) >= 11:
                    card_values.append(11)
                else:
                    card_values.append(1)
        return sum(card_values)

    def show_cards(self, player_cards):
        for i in self.player_cards:
            if i[0] == 's':
                print('------------')
                print(f'|{i[1:]}         |')
                print('|          |')
                print('| Spade -  |')
                print('|          |')
                print(f'|         {i[1:]}|')
                print('------------')
            if i[0] == 'h':
                print('------------')
                print(f'|{i[1:]}         |')
                print('|          |')
                print('| Heart -  |')
                print('|          |')
                print(f'|         {i[1:]}|')
                print('------------')
            if i[0] == 'd':
                print('------------')
                print(f'|{i[1:]}         |')
                print('|          |')
                print('| Diamond -|')
                print('|          |')
                print(f'|         {i[1:]}|')
                print('------------')
            if i[0] == 'c':
                print('------------')
                print(f'|{i[1:]}         |')
                print('|          |')
                print('| clubs -  |')
                print('|          |')
                print(f'|         {i[1:]}|')
                print('------------')


def card_suffle(fiftytwo_cards):
    random.shuffle(fiftytwo_cards)
    random.shuffle(fiftytwo_cards)
    return fiftytwo_cards

def card_distribute_dealer(set_cards):
    global set_of_cards
    dealer_cards.append(set_of_cards.pop())

def show_cards_dealer(dealer_cards):
    for i in dealer_cards:
        if i[0] == 's':
            print('------------')
            print(f'|{i[1:]}         |')
            print('|          |')
            print('| Spade -  |')
            print('|          |')
            print(f'|         {i[1:]}|')
            print('------------')
        if i[0] == 'h':
            print('------------')
            print(f'|{i[1:]}         |')
            print('|          |')
            print('| Heart -  |')
            print('|          |')
            print(f'|         {i[1:]}|')
            print('------------')
        if i[0] == 'd':
            print('------------')
            print(f'|{i[1:]}         |')
            print('|          |')
            print('| Diamond -|')
            print('|          |')
            print(f'|         {i[1:]}|')
            print('------------')
        if i[0] == 'c':
            print('------------')
            print(f'|{i[1:]}         |')
            print('|          |')
            print('| clubs -  |')
            print('|          |')
            print(f'|         {i[1:]}|')
            print('------------')

def check_value_of_dealercards(dealer_cards):
    card_values = []
    for i in dealer_cards:
        if i[1:] in ['J', 'Q', 'K']:
            card_values.append(10)
        elif i[1:] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            card_values.append(int(i[1:]))
        else:
            if (21 - sum(card_values)) >= 11:
                card_values.append(11)
            else:
                card_values.append(1)
    return sum(card_values)

def populate_cards(card_types):
    cards_fiftytwo = []
    for i in card_types:
        for j in range(1, 11):
            if j == 1:
                cards_fiftytwo.append(i + 'A')
            else:
                cards_fiftytwo.append(i+str(j))
        cards_fiftytwo.append(i+'J')
        cards_fiftytwo.append(i+'Q')
        cards_fiftytwo.append(i+'K')
    return cards_fiftytwo

def card_distribution(players_list, set_of_cards):
    for i in players_list.values():
        i.card_distribute(set_of_cards)
    card_distribute_dealer(set_of_cards)
    for i in players_list.values():
        i.card_distribute(set_of_cards)
        print("#######################################")
        print("#Player {} cards are displayed below#".format(i.name))
        print("#######################################")
        i.show_cards(i.player_cards)
        print("Total value of your cards is {}".format(i.value_of_cards(i.player_cards)))
    card_distribute_dealer(set_of_cards)
    print("#######################################")
    print("#Dealer first card is displayed below#")
    print("#######################################")
    show_cards_dealer([dealer_cards[0]])


temp_cards = populate_cards(card_types)
set_of_cards = card_suffle(temp_cards)
print(set_of_cards)
set_of_cards.reverse()

number_players = int(input("Choose number of players who wish to play BlackJack\n"))
for i in range(1, number_players + 1):
    name = input("Enter Player+{} name: ".format(str(i)))
    bet = int(input("Enter your betting amount: "))
    player_cards = []
    players_list[str(i)] = Blackjack(name, bet, player_cards,0)

while 1:
    card_distribution(players_list, set_of_cards)
    if check_value_of_dealercards(dealer_cards) == 21:
        print("JackPot for Dealer he got 21")
        print("#######################################")
        print("#Dealer cards are displayed below#")
        print("#######################################")
        show_cards_dealer(dealer_cards)
        for i in players_list.values():
            print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
        if int(input("Do you wish to continue? Enter 0 or 1")):
            dealers_cards = []
            for i in players_list.values():
                i.player_cards = []
            continue
        else:
            print("*********Bye***** Bye*****")
            quit()
    else:
        print("Dealer doesn't have 21")
        count_number_players_greater_21 = 0
        players_on_stay = []
        for i in players_list.values():
            while 1:
                if i.value_of_cards(i.player_cards) == 21:
                    print(f"Jackpot for player {i.name}")
                    print("#######################################")
                    print("#Player {} cards are displayed below#".format(i.name))
                    print("#######################################")
                    i.show_cards(i.player_cards)
                    print(f"Player {i.name} Total gains or loss is {i.calculate_wins()}")
                    i.player_cards = []
                    break
                if i.value_of_cards(i.player_cards) < 21:
                    hit_stand_split = int(input(f"Player {i.name}, press 1 for hit, press 2 for stand, press 3 for split"))
                    if hit_stand_split == 1:
                        i.card_distribute(set_of_cards)
                        print("#######################################")
                        print("#Player {} cards are displayed below#".format(i.name))
                        print("#######################################")
                        i.show_cards(i.player_cards)
                        print("Total value of your cards is {}".format(i.value_of_cards(i.player_cards)))
                        continue
                    if hit_stand_split == 2:
                        players_on_stay.append(i)
                        print(f"Player {i.name} has opted for stay on value {i.value_of_cards(i.player_cards)}")
                        print("#######################################")
                        print("#Player {} cards are displayed below#".format(i.name))
                        print("#######################################")
                        i.show_cards(i.player_cards)
                        break
                    if hit_stand_split == 3:
                        pass
                if i.value_of_cards(i.player_cards) > 21:
                    count_number_players_greater_21 = count_number_players_greater_21 + 1
                    print(f"Player {i.name} cards value is more than 21")
                    print("#######################################")
                    print("#Player {} cards are displayed below#".format(i.name))
                    print("#######################################")
                    i.show_cards(i.player_cards)
                    print(f"Player {i.name} Total gains or loss is {i.calculate_loss()}")
                    i.player_cards = []
                    break
    if count_number_players_greater_21 == number_players:
        print("All players lost and Dealer Won")
        dealers_cards = []
        for i in players_list.values():
            i.player_cards = []
        if int(input("Do you wish to continue? Enter 0 or 1")):
            continue
        else:
            print("*********Bye***** Bye*****")
            quit()
    else:
        print("#######################################")
        print("#Dealer cards are displayed below######")
        print("#######################################")
        show_cards_dealer(dealer_cards)
        while 1:
            if check_value_of_dealercards(dealer_cards) > 21:
                print("Dealer lost the game")
                print("#######################################")
                print("#Dealer cards are displayed below######")
                print("#######################################")
                show_cards_dealer(dealer_cards)
                for i in players_on_stay:
                    print(f"Player {i.name} Total Gains or Loss is {i.calculate_wins()}")
                    i.player_cards = []
                players_on_stay = []
                dealers_cards = []
                if int(input("Do you wish to continue? Enter 0 or 1")):
                    break
                else:
                    print("*********Bye***** Bye*****")
                    quit()
            if check_value_of_dealercards(dealer_cards) == 21:
                print("JackPot for Dealer he got 21")
                print("#######################################")
                print("#Dealer cards are displayed below#")
                print("#######################################")
                show_cards_dealer(dealer_cards)
                dealers_cards = []
                for i in players_on_stay:
                    print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
                    i.player_cards = []
                players_on_stay = []
                if int(input("Do you wish to continue? Enter 0 or 1")):
                    break
                else:
                    print("*********Bye***** Bye*****")
                    quit()

            if check_value_of_dealercards(dealer_cards) < 21:
                count_negative = 0
                count_positive = 0
                for i in players_on_stay:
                    if check_value_of_dealercards(dealer_cards) - i.value_of_cards(i.player_cards) < 0:
                        count_negative = count_negative + 1
                    if check_value_of_dealercards(dealer_cards) - i.value_of_cards(i.player_cards) > 0:
                        count_positive = count_positive + 1

                if (count_positive < count_negative) and (21 - check_value_of_dealercards(dealer_cards)) >= 6:
                    card_distribute_dealer(set_of_cards)
                    print("Dealer went for hit as he is having less than 21")
                    print("#######################################")
                    print("#Dealer cards are displayed below#")
                    print("#######################################")
                    show_cards_dealer(dealer_cards)
                    continue

                if (count_positive < count_negative) and (21 - check_value_of_dealercards(dealer_cards)) < 6:
                    print("Dealer decided to stay and no more hits")
                    for i in players_on_stay:
                        if i.value_of_cards(i.player_cards) > check_value_of_dealercards(dealers_cards):
                            print(f"Player {i.name} loss or gain is {i.calculate_win()}")
                        elif i.value_of_cards(i.player_cards) == check_value_of_dealercards(dealers_cards):
                            print(f"No Loss or Gain for player {i.name}")
                        else:
                            print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
                    dealers_cards = []
                    for i in players_on_stay:
                        print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
                        i.player_cards = []
                    players_on_stay = []
                    if int(input("Do you wish to continue? Enter 0 or 1")):
                        break
                    else:
                        print("*********Bye***** Bye*****")
                        quit()

                if (count_positive > count_negative) and (21 - check_value_of_dealercards(dealer_cards)) < 6:
                    print("Dealer decided to stay and no more hits")
                    for i in players_on_stay:
                        if i.value_of_cards(i.player_cards) > check_value_of_dealercards(dealers_cards):
                            print(f"Player {i.name} loss or gain is {i.calculate_win()}")
                        elif i.value_of_cards(i.player_cards) == check_value_of_dealercards(dealers_cards):
                            print(f"No Loss or Gain for player {i.name}")
                        else:
                            print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
                    dealers_cards = []
                    for i in players_on_stay:
                        print(f"Player {i.name} loss or gain is {i.calculate_loss()}")
                        i.player_cards = []
                    players_on_stay = []
                    if int(input("Do you wish to continue? Enter 0 or 1")):
                        break
                    else:
                        print("*********Bye***** Bye*****")
                        quit()

                if count_positive > count_negative and (21 - check_value_of_dealercards(dealer_cards)) >= 6:
                    card_distribute_dealer(set_of_cards)
                    print("Dealer went for hit as he is having less than 21")
                    print("#######################################")
                    print("#Dealer cards are displayed below#")
                    print("#######################################")
                    show_cards_dealer(dealer_cards)
                    continue

                if count_positive == count_negative and (21 - check_value_of_dealercards(dealer_cards)) >= 6:
                    card_distribute_dealer(set_of_cards)
                    print("Dealer went for hit as he is having less than 21")
                    print("#######################################")
                    print("#Dealer cards are displayed below#")
                    print("#######################################")
                    show_cards_dealer(dealer_cards)
                    continue

                if count_positive == count_negative and (21 - check_value_of_dealercards(dealer_cards)) < 6:
                    print("Dealer decided to stay and no loss no gain for rest of the players")
                    print(f"No Loss or Gain for player {i.name}")
                    dealers_cards = []
                    for i in players_on_stay:
                        i.player_cards = []
                    players_on_stay = []
                    if int(input("Do you wish to continue? Enter 0 or 1")):
                        break
                    else:
                        print("*********Bye***** Bye*****")
                        quit()