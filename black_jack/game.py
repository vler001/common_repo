import random
from Deck import *


def blackjack_game(deck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0

    def play_again():
        again = input("Бажаєте нову гру? (y/n) : ").lower()
        if again == "y":
            blackjack_game(deck)
        else:
            print("До зустрічі!")
            exit()
    '''Початкова роздача  карт гравцеві та дилеру.
    Друга карта для дилера повинна залишатися невідомою.'''
    while len(player_cards) < 2:
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value
        '''Якщо зразу гравцю випило два Тузи, перше значення рахується як 1 очко'''
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
        print("Карти гравця: ")
        print_cards(player_cards, False)
        print("Рахунок гравця = ", player_score)
        input()

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value
        print("Карти дилера: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("Рахунок дилера = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("Рахунок дилера = ", dealer_score - dealer_cards[-1].card_value)
        '''Якщо зразу дилеру випило два Тузи, друге значення рахується як 1 очко'''
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
        input()

    if player_score == 21:
        print("У гравця BLACKJACK")
        print("Ви виграли!!!!")
        play_again()

    print("Карти дилера: ")
    print_cards(dealer_cards[:-1], True)
    print("Рахунок дилера = ", dealer_score - dealer_cards[-1].card_value)
    print()
    print("Карти гравця: ")
    print_cards(player_cards, False)
    print("Рахунок гравця = ", player_score)

    # Рух по рахунку гравця. Поки менше очок ніж 21 очко - дилер пропонує карту
    while player_score < 21:
        choice = input("Введіть H щоб взяти карту, або S коли досить карт : ")

        # перевірка від невірного вводу гравцем
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Не вірний вибір!! Повторіть вибір")

        elif choice.upper() == 'H': # дилер дає ще карту
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
            player_score += player_card.card_value

            # Оновлення рахунку гравця, якщо є туз потім
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1

            print("Карти дилера: ")
            print_cards(dealer_cards[:-1], True)
            print("Рахунок дилера = ", dealer_score - dealer_cards[-1].card_value)
            print()
            print("Карти гравця: ")
            print_cards(player_cards, False)
            print("Рахунок гравця = ", player_score)

        elif choice.upper() == 'S':# Не беремо більше карт
            break

    print("Карти гравця: ")
    print_cards(player_cards, False)
    print("Рахунок гравця = ", player_score)
    print()
    print("Дилер розкриває карти....")
    print("Карти дилера: ")
    print_cards(dealer_cards, False)
    print("Рахунок дилера = ", dealer_score)

    if player_score == 21:
        print("У гравця-  BLACKJACK")
        play_again()

    elif player_score > 21:
        print("Ви програли!!! Гра закінчена!!!")
        play_again()
    input()

    # Рух по рахунку дилера
    while dealer_score < 17:
        print("Дилер бере карту.....")
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value
        # Оновлення рахунку дилера, якщо є туз потім
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        print("Карти гравця: ")
        print_cards(player_cards, False)
        print("Рахунок гравця = ", player_score)
        print()
        print("Карти дилера: ")
        print_cards(dealer_cards, False)
        print("Рахунок дилера = ", dealer_score)
        input()

    if dealer_score > 21:
        print("Дилер програв. Ви виграли!!!")
        quit()
    elif dealer_score == 21:
        print("У дилера - BLACKJACK!!! Ви програли.")
        play_again()
    elif dealer_score == player_score:
        print("Нічия гра!!!!")
        play_again()
    elif player_score > dealer_score:
        print("Ви виграли!!!")
        play_again()
    else:
        print("Дилер виграв.")
        play_again()


