from ctypes import addressof


from datetime import datetime

class Client:
    def __init__(self, first_name, last_name, address, birthday) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        year, month, day = int(birthday[:4]), int(birthday[5:7]), int(birthday[8:11])
        self.birthday = datetime(year, month, day)
    
    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name
    
    def get_address(self) -> str:
        return self.address
    
    def get_birthday(self) -> datetime:
        return self.birthday

    # TODO: this is not a proven method to calculate the age. It just serves
    # the purpose of this assignment
    def get_age(self) -> int:
        today = datetime.now().date()
        age = int((today - self.get_birthday().date()).days / 365.25)
        return age