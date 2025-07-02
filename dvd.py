



from models.library_item import LibraryItem
from  models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration):
        super().__init__(item_id, title, author)
        self.duration = duration  

    def display_info(self):
        print(f"[DVD] {self.title} by {self.author} - Duration: {self.duration} mins - {'Available' if self.available else 'Unavailable'}")

    def reserve(self, user):
        if not self.reserved_by:
            self.reserved_by = user.user_id
        else:
            raise Exception("Item already reserved")
