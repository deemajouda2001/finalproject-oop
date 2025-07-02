

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item_id):
        if item_id not in self.borrowed_items:
            self.borrowed_items.append(item_id)

    def return_item(self, item_id):
        if item_id in self.borrowed_items:
            self.borrowed_items.remove(item_id)

    def __str__(self):
        return f"User({self.user_id}) {self.name}"
