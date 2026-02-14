class Wallet:

    @staticmethod
    def deposit(manager, amount):
        manager.balance += amount

    @staticmethod
    def withdraw(manager, amount):
        if amount <= manager.balance:
            manager.balance -= amount
            return True
        return False
    
