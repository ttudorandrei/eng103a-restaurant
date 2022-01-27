class Table:
    def __init__(self, number_of_people):
        self.name = "Table"
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        for i in self.bill:
            if i and i["item"] == item:
                i["quantity"] += quantity
                print("first condition true")
            elif i["item"] != item:
                print("item not in list")
                self.bill.insert({"item": item, "price": price, "quantity": quantity})

        if len(self.bill) == 0:
            self.bill.append({"item": item, "price": price, "quantity": quantity})


    def remove(self, item, price, quantity=1):
        for i in self.bill:
            if i and i["item"] == item:
                i["quantity"] -= quantity
                print("first condition true")
            elif i["item"] != item:
                return False

        if len(self.bill) == 0:
            return False

