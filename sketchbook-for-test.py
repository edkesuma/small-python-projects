class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    def __str__(self):
        return self.name + " " + self.membership

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

customer1 = Customer('Edrick', 'Gold')
customer2 = Customer('Rando1', 'Bronze')
customers = customer1, customer2
print(customer1)
Customer.print_all_customers(customers)
