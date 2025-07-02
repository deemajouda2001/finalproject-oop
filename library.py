
import json
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
from models.user import User
from exceptions.exceptions import ItemNotAvailableError,  UserNotFoundError,ItemNotFoundError
class Library:
    def __init__(self):
        self.users = {}  
        self.items = {}  

    def load_data(self, users_file, items_file):
        try:
            with open(users_file) as f:
                for u in json.load(f):
                    self.users[u["user_id"]] = User(**u)

            with open(items_file) as f:
                for i in json.load(f):
                    item_type = i.get("__type__")
                    if item_type == "Book":
                        self.items[i["item_id"]] = Book(**i)
                    elif item_type == "DVD":
                        self.items[i["item_id"]] = DVD(**i)
                    elif item_type == "Magazine":
                        self.items[i["item_id"]] = Magazine(**i)
        except Exception as e:
            print("Error loading data:", e)

    def save_data(self, users_file, items_file):
        try:
            with open(users_file, 'w') as f:
                json.dump([u.__dict__ for u in self.users.values()], f, indent=2)
            with open(items_file, 'w') as f:
                item_list = []
                for item in self.items.values():
                    d = item.__dict__.copy()
                    d["__type__"] = type(item).__name__
                    item_list.append(d)
                json.dump(item_list, f, indent=2)
        except Exception as e:
            print("Error saving data:", e)

    def add_user(self, user: User):
        self.users[user.user_id] = user

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def add_item(self, item):
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def borrow_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found.")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found.")

        item = self.items[item_id]
        if not item.available:
            raise ItemNotAvailableError("Item not available.")

        user = self.users[user_id]
        user.borrow_item(item_id)
        item.available = False

    def return_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found.")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found.")

        user = self.users[user_id]
        if item_id not in user.borrowed_items:
            raise Exception("Item not borrowed by this user.")

        user.return_item(item_id)
        self.items[item_id].available = True

    def reserve_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found.")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found.")

        item = self.items[item_id]
        user = self.users[user_id]

        if hasattr(item, "reserve"):
            item.reserve(user)
        else:
            raise Exception("This item cannot be reserved.")
