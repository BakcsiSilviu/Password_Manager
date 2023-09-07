from random import choice, randint

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Generator():
    def __init__(self):
        self.letters = ''
        self.numbers = ''
        self.symbols = ''
        self.final_password = ''
        self.extract_letters()
        self.extract_numbers()
        self.extract_symbols()
        self.create_password()

    def extract_letters(self):
        for _ in range(randint(5,7)):
            self.letters += choice(LETTERS)

    def extract_numbers(self):
        for _ in range(randint(4,7)):
            self.numbers += choice(NUMBERS)

    def extract_symbols(self):
        for _ in range(randint(1,5)):
            self.symbols += choice(SYMBOLS)

    def create_password(self):
        appended_password = [el for el in self.letters+self.numbers+self.symbols]
        for _ in range(0, len(appended_password) - 1):
            self.final_password += choice(appended_password)
            appended_password.remove(self.final_password[-1])
