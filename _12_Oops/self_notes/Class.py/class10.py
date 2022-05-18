
class Purchase_order:

    def __init__(self, date,  item1, quantity, description, unit_price, total, company_name="VN2 ",  address ="I GATE KUNDANAHALLI",):
        self.date = date
        self.company_name =company_name
        self.address =address
        self.item1 = item1
        self.quantity = quantity
        self.description = description
        self.unit_price = unit_price
        self.total = total


    def purchese_details(self):
        print("Purchase order is ", self.date, self.company_name, self.address, self.item1, self.quantity, self.description, self.unit_price, self.total)

company1 = Purchase_order("05-May-2022","Python software", 1, "fill", 12000, 12000)

company1.purchese_details()

