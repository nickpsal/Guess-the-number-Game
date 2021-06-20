import random


def computer_number():
    computer_num = random.randint(1, 200)
    return computer_num


def user_input() :
    while True:
        try:
            number = int(input("Δωσε έναν αριθμό μεταξύ 1 και 200 "))
            break
        except ValueError:
            print("Error")
    return number


def play_game(computer_num):
    counter = 1
    while True:
        number = user_input()
        if number == computer_num :
            print("Συγχαρητήρια τον βρήκες με %s" % counter)
            break
        elif number > computer_num :
            print("Ο Αριθμός που δώσατε είναι μεγασλύτερος απο αυτον του υπολογιστη")
            counter += 1
        elif number < computer_num :
            counter += 1
            print("Ο Αριθμός που δώσατε είναι μικρότερος απο αυτον του υπολογιστη")


def main():
    print("GUESS THE NUMBER GAME")
    print("Ο υπολογιστής επιλέγει ένα νούμερο μεταξ΄λυ 1 και 200")
    print("και ο χρήστης προσπαθεί να τον μαντέψει")
    computer_num = computer_number()
    play_game(computer_num)


main()