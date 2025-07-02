


from models.library_item import LibraryItem
from models.reservable import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author)
        self.genre = genre

    def display_info(self):
        print(f"[Book] {self.title} by {self.author} - Genre: {self.genre} - {'Available' if self.available else 'Unavailable'}")

    def reserve(self, user):
        if not self.reserved_by:
            self.reserved_by = user.user_id
        else:
            raise Exception("Item already reserved")


