# Olympic Basketball Text-Based Adventure Game
# Author: DeLaun Robinson

ROOMS = {
    "Preliminary Round 1": {"West": "Preliminary Round 2"},
    "Preliminary Round 2": {"East": "Preliminary Round 1", "South": "Preliminary Round 3", "item": "Greece"},
    "Preliminary Round 3": {"North": "Preliminary Round 2", "South": "Semifinals", "West": "Quarterfinals", "item": "Germany"},
    "Quarterfinals": {"East": "Preliminary Round 3", "item": "South Sudan"},
    "Semifinals": {"North": "Preliminary Round 3", "South": "Gold Medal Match", "East": "Bronze Medal Match", "item": "Serbia"},
    "Bronze Medal Match": {"West": "Semifinals", "item": "Bronze Medal"},
    "Gold Medal Match": {"North": "Semifinals", "East": "Victory Hall", "item": "Gold Medal"},
    "Victory Hall": {},
}

WIN_ITEMS = {"Greece", "Germany", "South Sudan", "Serbia", "Gold Medal"}
VILLAIN_ROOM = "Bronze Medal Match"


def show_instructions() -> None:
    print("\nOlympic Basketball Game")
    print("Collect all required items to win the gold medal.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to inventory: get <item name>")
    print("Avoid the Bronze Medal Match until you have collected all items.")
    print("Type 'exit' to quit.\n")


def show_status(current_room: str, inventory: set[str]) -> None:
    print("----------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {sorted(inventory)}")
    item = ROOMS.get(current_room, {}).get("item")
    if item and item not in inventory:
        print(f"You see a {item}")


def normalize_item(name: str) -> str:
    return " ".join(word.capitalize() for word in name.strip().split())


def main() -> None:
    current_room = "Preliminary Round 1"
    inventory: set[str] = set()
    show_instructions()

    while True:
        show_status(current_room, inventory)

        if current_room == VILLAIN_ROOM and not WIN_ITEMS.issubset(inventory):
            print("NOM NOM...GAME OVER!")
            break

        if current_room == "Victory Hall" and WIN_ITEMS.issubset(inventory):
            print("Congrats, you have won the Gold Medal for your country!")
            break

        move = input("Enter your move: ").strip()
        move_lower = move.lower()

        if move_lower == "exit":
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        if move_lower.startswith("go "):
            direction = move[3:].strip().capitalize()
            if direction in ROOMS[current_room]:
                current_room = ROOMS[current_room][direction]
            else:
                print("You can't go that way!")
            continue

        if move_lower.startswith("get "):
            item_name = normalize_item(move[4:])
            room_item = ROOMS.get(current_room, {}).get("item")
            if room_item == item_name and item_name not in inventory:
                inventory.add(item_name)
                print(f"You have collected the {item_name}!")
            else:
                print("There's no item to collect here.")
            continue

        print("Invalid command!")


if __name__ == "__main__":
    main()
