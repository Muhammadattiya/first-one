class person:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__club = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_club(self, club):
        self.__club = club

    def get_club(self):
        return self.__club

    def display_details(self):
        print(f"Player's name: {self.__name}")
        print(f"Player's age: {self.__age}")
        print(f"Player's club: {self.__club}")


class Player(person):
    def __init__(self):
        super().__init__()
        self.__position = ""

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position


class Manager(person):
    def __init__(self):
        super().__init__()

    # List to store Player objects


players = []
manager = []


def add_player():
    # Create a Player object
    player = Player()

    # Get user input
    name = input("Enter the player's name: ")
    age = int(input("Enter the player's age: "))
    club = input("Enter the player's club: ")
    position = input("Enter the player's position: ")

    # Set attributes using setters
    player.set_name(name)
    player.set_age(age)
    player.set_club(club)
    player.set_position(position)

    # Add the player to the list
    players.append(player)


def delete_player():
    name = input("Enter the name of the player to delete: ")
    for player in players:
        if player.get_name() == name:
            players.remove(player)
            print(f"{name} has been removed from the list.")
            return
    print(f"No player found with the name {name}.")


def display_all_players():
    if not players:
        print("No players in the list.")
    else:
        for player in players:
            player.display_details()
            print(f"Player's Position: {player.get_position()}")
            print("-----------")


def add_manager():
    manager = Manager()


while True:
    # Show the menu to the user
    print("-" * 50)
    print("Menu:")
    print("1. Add a new player")
    print("2. Add a new Manager")
    print("3. Delete a player")
    print("4. View all players")
    print("5. Exit")
    print("-" * 10)
    choice = input("Enter your choice (1/2/3/4/5): ")
    print("-" * 50)

    if choice == '1':
        add_player()
    elif choice == '2':
        add_manager()
    elif choice == '3':
        delete_player()
    elif choice == '4':
        display_all_players()
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")

print("Goodbye!")