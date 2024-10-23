class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être inférieur à 0.")
        self._balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être inférieur à 0.")
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError("Solde insuffisant.")
        self._balance -= amount

account = Account()
account.balance = 100

try:
    account.withdraw(150)  # Doit lever une exception
except ValueError:
    print("Solde insuffisant")