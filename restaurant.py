class Table:
    def __init__(self, number_of_people):
        self.name = "Table"
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        for i in self.bill:
            if i and i["item"] == item:
                i["quantity"] += quantity
            # i["item"] != item:
            else:
                self.bill.append({"item": item, "price": float(price), "quantity": quantity})

        if len(self.bill) == 0:
            self.bill.append({"item": item, "price": float(price), "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for i in self.bill:
            if i and i["item"] == item:
                i["quantity"] -= quantity
            elif i["item"] != item and i["price"] != price:
                return False

        if len(self.bill) == 0:
            return False

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i["quantity"] * float(i["price"])
        return subtotal

    def get_total(self, service_charge=0.10):
        total = 0
        subtotal = 0
        for i in self.bill:
            subtotal += i["quantity"] * float(i["price"])
            total = subtotal + subtotal * service_charge
        return {'Sub Total': f"£{subtotal}", 'Service Charge': f"£{subtotal * service_charge}", 'Total': total}

    def split_bill(self):
        return int(self.get_total()["Total"]) / self.number_of_people


table02 = Table(2)

table02.order('Food1', 10.00, 3)
table02.order('Food2', 20.00, 1)
table02.order('Food3', 0.50, 1)

table02.get_subtotal()
