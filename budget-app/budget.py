# ======  class Category =========
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def check_funds(self, amount: float):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total

    def transfer(self, amount: float, new_category):
        if self.get_balance() < amount:
            return False
        else:
            self.withdraw(amount, f"Transfer to {new_category.name}")
            new_category.deposit(amount, f"Transfer from {self.name}")
            return True

    def __str__(self):
        as_str = '{:*^30}'.format(self.name) + '\n'
        for item in self.ledger:
            as_str += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        as_str += f"Total: {format(self.get_balance(), '.2f')}"
        return as_str


# =======  chart function ========
def create_spend_chart(categories):
    names = []
    spent = []
    spent_percents = []

    for category in categories:
        total = 0
        for x in category.ledger:
            if x['amount'] < 0:
                total -= x['amount']
        spent.append(round(total, 2))
        names.append(category.name)
    for category_spent in spent:
        spent_percents.append(round(category_spent / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"

    for label in range(100, -10, -10):
        graph += '{:>3}'.format(str(label)) + '{:<2}'.format("|")
        for percents in spent_percents:
            if percents >= label:
                graph += '{:<3}'.format("o")
            else:
                graph += '{:<3}'.format("")
        graph += "\n"

    graph += '{:>8}'.format("----") + ("---" * (len(names) - 1))
    graph += '{:<6}'.format("\n")

    longest_name = 0

    for name in names:
        if longest_name < len(name):
            longest_name = len(name)

    for i in range(longest_name):
        for name in names:
            if len(name) > i:
                graph += name[i] + '{:<2}'.format("")
            else:
                graph += '{:<3}'.format("")
        if i < longest_name - 1:
            graph += '{:<6}'.format('\n')

    return graph
