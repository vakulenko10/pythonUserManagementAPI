import json

def main_menu():
    print("1. Dodaj nowego użytkownika")
    print("2. Wyświetl listę użytkowników")
    print("3. Zapisz użytkowników do pliku")
    print("4. Wczytaj użytkowników z pliku")
    print("5. Edytuj użytkownika")
    print("6. Usuń użytkownika")
    print("7. Wyszukaj użytkownika")
    print("8. Sortuj użytkowników")
    print("9. Wyjście")

    choice = input("Wybierz opcję: ")
    return choice

def add_user(users):
    if users:
        user_id = users[-1]["id"] + 1
    else:
        user_id = 1
    name = input("Podaj imię użytkownika: ")
    lastname = input("Podaj nazwisko użytkownika: ")
    age = input("Podaj wiek użytkownika: ")
    users.append({"id": user_id, "name": name, "lastname": lastname, "age": age})
    print("Użytkownik dodany pomyślnie.")

def display_users(users):
    if not users:
        print("Brak użytkowników.")
    else:
        for user in users:
            print(f"\t id: {user['id']}, imie: {user['name']}, nazwisko: {user['lastname']}, wiek: {user['age']} lat")

def save_to_file(users):
    with open("users.json", "w") as file:
        json.dump(users, file)
    print("Dane zapisane do pliku 'users.json'.")

def load_from_file():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        print("Dane wczytane z pliku 'users.json'.")
        return users
    except FileNotFoundError:
        print("Plik 'users.json' nie istnieje.")
        return []

def edit_user(users):
    user_id = int(input("Podaj ID użytkownika do edycji: "))
    for user in users:
        if user['id'] == user_id:
            user['name'] = input(f"Podaj nowe imię użytkownika (obecne: {user['name']}): ") or user['name']
            user['lastname'] = input(f"Podaj nowe nazwisko użytkownika (obecne: {user['lastname']}): ") or user['lastname']
            user['age'] = input(f"Podaj nowy wiek użytkownika (obecny: {user['age']}): ") or user['age']
            print("Dane użytkownika zaktualizowane pomyślnie.")
            return
    print("Nie znaleziono użytkownika o podanym ID.")

def delete_user(users):
    user_id = int(input("Podaj ID użytkownika do usunięcia: "))
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(i)
            print("Użytkownik usunięty pomyślnie.")
            return
    print("Nie znaleziono użytkownika o podanym ID.")

def search_user(users):
    search_term = input("Podaj imię lub nazwisko do wyszukania: ").lower()
    results = [user for user in users if search_term in user['name'].lower() or search_term in user['lastname'].lower()]
    if results:
        for user in results:
            print(f"\t {user['id']}) {user['name']}, {user['lastname']}, {user['age']} lat")
    else:
        print("Nie znaleziono użytkowników.")

def sort_users(users):
    print("1. Sortuj po imieniu")
    print("2. Sortuj po nazwisku")
    print("3. Sortuj po wieku")
    print("4. Sortuj po id")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        users.sort(key=lambda user: user['name'].lower())
    elif choice == "2":
        users.sort(key=lambda user: user['lastname'].lower())
    elif choice == "3":
        users.sort(key=lambda user: int(user['age']))
    elif choice == "4":
        users.sort(key=lambda user: int(user['id']))
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        return

    print("Lista użytkowników posortowana pomyślnie.")

def main():
    users = []
    while True:
        choice = main_menu()

        if choice == "1":
            add_user(users)
        elif choice == "2":
            display_users(users)
        elif choice == "3":
            save_to_file(users)
        elif choice == "4":
            users = load_from_file()
        elif choice == "5":
            edit_user(users)
        elif choice == "6":
            delete_user(users)
        elif choice == "7":
            search_user(users)
        elif choice == "8":
            sort_users(users)
        elif choice == "9":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
