class Bill:
    """
    Object that contains data about a bill, such as total amount owed
    and the pay period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays
    a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmates):
        weight = self.days_in_house / sum(flatmate.days_in_house for flatmate in flatmates)
        return round(weight * bill.amount, 2)
