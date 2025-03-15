import tkinter as tk
from tkinter import messagebox
import random

# Lista pytań i wyzwań
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

# Funkcja dodawania graczy
def gamers():
    def add_player():
        name = entry.get().strip()
        if len(name) > 2:
            gamer_list.append(name.capitalize())
            players_listbox.insert(tk.END, name.capitalize())
            entry.delete(0, tk.END)
            error_label.config(text="")
        else:
            error_label.config(text="Podaj dłuższą nazwę!", fg="red")

    window = tk.Toplevel(root)
    window.title("Dodaj graczy")
    window.configure(bg="#1e1e1e")

    label = tk.Label(window, text="Wprowadź nazwę gracza:", font=("Helvetica", 14), fg="#ffffff", bg="#1e1e1e")
    label.pack(pady=20)

    entry = tk.Entry(window, font=("Helvetica", 14), bg="#333333", fg="#ffffff", insertbackground="white")
    entry.pack(pady=10)

    add_button = tk.Button(window, text="Dodaj Gracza", font=("Helvetica", 14), bg="#007bff", fg="#ffffff", command=add_player)
    add_button.pack(pady=20)

    players_listbox = tk.Listbox(window, font=("Helvetica", 12), bg="#333333", fg="#ffffff", height=6)
    players_listbox.pack(pady=10)

    error_label = tk.Label(window, text="", font=("Helvetica", 12), fg="red", bg="#1e1e1e")
    error_label.pack(pady=10)

    done_button = tk.Button(window, text="Gotowe", font=("Helvetica", 14), bg="#28a745", fg="#ffffff", command=window.destroy)
    done_button.pack(pady=10)

# Funkcja rozpoczęcia gry
def start_game():
    if len(gamer_list) < 2:
        messagebox.showerror("Błąd", "Potrzebujesz przynajmniej dwóch graczy.")
        return

    def play_game():
        def next_turn():
            if gamer_list:
                current_player = gamer_list[0]
                gamer_list.append(gamer_list.pop(0))  # Rotate players
                current_player_label.config(text=f"Teraz gra: {current_player}")
                user_choice = choice_var.get()

                if user_choice == "Prawda":
                    if list_of_questions:
                        question_index = random.randint(0, len(list_of_questions) - 1)
                        question_label.config(text=f"PRAWDA: {list_of_questions[question_index]}")
                        list_of_questions.pop(question_index)
                    else:
                        question_label.config(text="Brak pytań! Gra się kończy.")
                        action_button.config(state=tk.DISABLED)
                elif user_choice == "Wyzwanie":
                    if list_of_actions:
                        action_index = random.randint(0, len(list_of_actions) - 1)
                        action_label.config(text=f"WYZWANIE: {list_of_actions[action_index]}")
                        list_of_actions.pop(action_index)
                    else:
                        action_label.config(text="Brak wyzwań! Gra się kończy.")
                        action_button.config(state=tk.DISABLED)
                else:
                    question_label.config(text="Błędny wybór, robisz Prawdę i Wyzwanie")
                    if list_of_questions:
                        question_index = random.randint(0, len(list_of_questions) - 1)
                        question_label.config(text=f"PRAWDA: {list_of_questions[question_index]}")
                        list_of_questions.pop(question_index)
                    if list_of_actions:
                        action_index = random.randint(0, len(list_of_actions) - 1)
                        action_label.config(text=f"WYZWANIE: {list_of_actions[action_index]}")
                        list_of_actions.pop(action_index)

        game_window = tk.Toplevel(root)
        game_window.title("Gra Prawda czy Wyzwanie")
        game_window.configure(bg="#1e1e1e")

        current_player_label = tk.Label(game_window, text="Teraz gra: ", font=("Helvetica", 16), fg="#ffffff", bg="#1e1e1e")
        current_player_label.pack(pady=30)

        choice_var = tk.StringVar()
        choice_label = tk.Label(game_window, text="Wybierz: Prawda czy Wyzwanie", font=("Helvetica", 14), fg="#ffffff", bg="#1e1e1e")
        choice_label.pack(pady=10)

        pravda_button = tk.Radiobutton(game_window, text="Prawda", variable=choice_var, value="Prawda", font=("Helvetica", 14), fg="#ffffff", bg="#1e1e1e", selectcolor="#007bff", activebackground="#1e1e1e")
        pravda_button.pack(pady=10)

        wyzwanie_button = tk.Radiobutton(game_window, text="Wyzwanie", variable=choice_var, value="Wyzwanie", font=("Helvetica", 14), fg="#ffffff", bg="#1e1e1e", selectcolor="#007bff", activebackground="#1e1e1e")
        wyzwanie_button.pack(pady=10)

        question_label = tk.Label(game_window, text="Prawda: ", font=("Helvetica", 12), fg="#ffffff", bg="#1e1e1e")
        question_label.pack(pady=10)

        action_label = tk.Label(game_window, text="Wyzwanie: ", font=("Helvetica", 12), fg="#ffffff", bg="#1e1e1e")
        action_label.pack(pady=10)

        action_button = tk.Button(game_window, text="Następna tura", font=("Helvetica", 14), bg="#007bff", fg="#ffffff", command=next_turn)
        action_button.pack(pady=20)

        next_round_button = tk.Button(game_window, text="Koniec gry", font=("Helvetica", 14), bg="#dc3545", fg="#ffffff", command=game_window.destroy)
        next_round_button.pack(pady=10)

# Główne okno aplikacji
root = tk.Tk()
root.title("Prawda czy Wyzwanie")
root.configure(bg="#1e1e1e")

main_label = tk.Label(root, text="Witaj w grze Prawda czy Wyzwanie!", font=("Helvetica", 24), fg="#ffffff", bg="#1e1e1e")
main_label.pack(pady=30)

start_button = tk.Button(root, text="Rozpocznij grę", font=("Helvetica", 16), bg="#28a745", fg="#ffffff", command=start_game)
start_button.pack(pady=20)

add_player_button = tk.Button(root, text="Dodaj graczy", font=("Helvetica", 16), bg="#007bff", fg="#ffffff", command=gamers)
add_player_button.pack(pady=20)

root.mainloop()
