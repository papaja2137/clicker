import random

list_of_questions = [
    "Jaką najdziwniejszą rzecz zjadłeś?",
    "Jakie jest twoje marzenie?",
    "Jak często myślisz o Imperium Rzymskim", 
    "Jaka jest twoja ulubiona Partia Polityczna",
    "Czy kiedykolwiek oszukiwałeś w grze",
    "Jaki jest twój ulubiony król Polski"
]

list_of_actions = [
    "Zrób 10 przysiadów",
    "Krzyknij przez okno",
    "Chodź jak pingwin przez 2 minuty",
    "Podskocz 5 razy na lewej nodze",
    "Zrób dziwną minę",
    "Nie śmiej się przez 10 minut"
]

gamer_list = []

def gamers(list):
    while True:
        name = input("Wprowadź nazwę gracza: ")
        if len(name) <= 2:
            print("Podaj dłuższą nazwę!")
            continue
        list.append(name.capitalize())
        if len(list) >= 2:
            need_next_player = input("Czy chcesz dodać kolejnego gracza Y/N: ").lower()
            if need_next_player == "y" or need_next_player == "yes":
                continue
        else:
            break

gamers(gamer_list)
print("Gracze: ", gamer_list)

def game(list_of_questions, list_of_actions, *args):
    while True:
        for gamer in args:
            print(f"Teraz gra: {gamer}")
            user_choice = input("Prawda czy Wyzwanie (P/N): ").lower()

            if user_choice == "p":
                if list_of_questions:  # Check if there are any questions left
                    question_index = random.randint(0, len(list_of_questions) - 1)
                    print("PRAWDA: ", list_of_questions[question_index])
                    list_of_questions.pop(question_index)
                else:
                    print("Brak pytań! Gra się kończy.")
                    return
            elif user_choice == "w":
                if list_of_actions:  # Check if there are any actions left
                    action_index = random.randint(0, len(list_of_actions) - 1)
                    print("WYZWANIE: ", list_of_actions[action_index])
                    list_of_actions.pop(action_index)
                else:
                    print("Brak wyzwań! Gra się kończy.")
                    return
            else:
                print("Błędny wybór, robisz Prawdę i Wyzwanie")
                if list_of_questions:
                    question_index = random.randint(0, len(list_of_questions) - 1)
                    print("PRAWDA: ", list_of_questions[question_index])
                    list_of_questions.pop(question_index)
                if list_of_actions:
                    action_index = random.randint(0, len(list_of_actions) - 1)
                    print("WYZWANIE: ", list_of_actions[action_index])
                    list_of_actions.pop(action_index)

        next_round = input("Nowa runda? (Y/N): ").lower()
        if next_round != "y":
            print("KONIEC GRY")
            break

gamers(gamer_list)
game(list_of_questions, list_of_actions, *gamer_list)