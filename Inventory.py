import Weapon as wpn


class Inventory:
    def __init__(self):
        self.wallet = Wallet()
        self.inv_dict = {"armor":  [],
                         "weapon": [],
                         "tool":   []}

    def add_weapon(self, name, damage, dmg_type, cost):
        self.inv_dict["weapon"].append(wpn.Weapon(name, damage, dmg_type, cost))


class Wallet:
    # Platinum = gold * 10
    # Gold = elecrtum * 2
    # Electrum = silver * 5
    # Silver = copper * 10
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def add_platinum(self, num_coins):
        self.__balance += num_coins * 1000

    def add_gold(self, num_coins):
        self.__balance += num_coins * 100

    def add_electrum(self, num_coins):
        self.__balance += num_coins * 20

    def add_silver(self, num_coins):
        self.__balance += num_coins * 10

    def add_copper(self, num_coins):
        self.__balance += num_coins

