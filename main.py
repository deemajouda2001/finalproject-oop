from models.library import Library
from models.magazine import Magazine
from models.library_item import LibraryItem
from exceptions.exceptions import ItemNotAvailableError,  UserNotFoundError,ItemNotFoundError



def main():
    library = Library()
    library.load_data("items.json", "users.json")

    while True:
        print("""
Welcome to the Library System
1. View all available items
2. Search item by title or type
3. Register as a new user
4. Borrow an item
5. Reserve an item
6. Return an item
7. Exit and Save
""")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                for item in library.items:
                    item.display_info()

            elif choice == "2":
                keyword = input("Enter title or type to search: ").lower()
                for item in library.items:
                    if keyword in item.title.lower() or keyword in item.__class__.__name__.lower():
                        item.display_info()

            elif choice == "3":
                name = input("Enter your name: ")
                library.add_user(name)

            elif choice == "4":
                user_id = input("Enter your User ID: ")
                item_id = input("Enter the Item ID to borrow: ")
                library.borrow_item(user_id, item_id)
                print("Item borrowed successfully.")

            elif choice == "5":
                user_id = input("Enter your User ID: ")
                item_id = input("Enter the Item ID to reserve: ")
                library.reserve_item(user_id, item_id)
                print("Item reserved successfully.")

            elif choice == "6":
                user_id = input("Enter your User ID: ")
                item_id = input("Enter the Item ID to return: ")
                library.return_item(user_id, item_id)
                print("Item returned successfully.")

            elif choice == "7":
                library.save_data("items.json", "users.json")
                print("Data saved")
                break

            else:
                print("Invalid option. Please enter a number between 1 and 7.")

        except (ItemNotFoundError, UserNotFoundError, ItemNotAvailableError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
