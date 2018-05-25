class Bar:
    clientCnt = 0

    def __init__(self, name):
        self.name = name
        self.amount_spent = 0
        self.dish = []
        Bar.clientCnt += 1

    def display_count(self):
            print("Total Visits %d" % Bar.clientCnt)

    def display_visit(self):
        print("Name : ", self.name)
        print("Amount spent: ", self.amount_spent)
        print("Dishes ordered: ")
        for i in self.dish:
            print(i)

    def add_dish(self, dish, price):
        self.dish.append(dish)
        self.amount_spent += price


bar1 = Bar("Artem")
bar1.add_dish("Beer", 5)
bar1.add_dish("Meat", 15)

bar2 = Bar("Olya")
bar2.add_dish("Pasta", 12)
bar2.add_dish("Vodka", 15)

bar3 = Bar("Vlad")
bar3.add_dish("Vodka", 15)
bar3.add_dish("Risotto", 15)

bar4 = Bar("Andrei")
bar4.add_dish("Wiskey", 20)
bar4.add_dish("Cola", 5)

bar1.display_visit()
print()
bar2.display_visit()
print()
bar3.display_visit()
print()
bar4.display_visit()
