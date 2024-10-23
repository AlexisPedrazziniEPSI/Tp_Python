class BankAccount:
    def __init__(self, balance):
        assert balance > 0, "Le compte doit avoir de l'argent"
        self.balance = balance

    def __add__(self, montant):
        self.balance += montant
        return self

    def __sub__(self, montant):
        self.balance -= montant
        return self

    def __str__(self):
        return f"Le solde du compte est de {self.balance} euros"

account = BankAccount(100)
account += 20
assert account.balance == 120

account -= 50
assert account.balance == 70