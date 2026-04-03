toppings_list1 = "pepperoni, sausage, mushrooms, onions, bell peppers, black olives, extra cheese, ham, pineapple, bacon, chicken"
toppings_lists = toppings_list1.split(", ")


class Pizza:
    def __init__(self, size="", crust_type="", toppings=None):
        self.size = size
        self.crust = crust_type
        if toppings is None:
            self.toppings = []
        else:
            self.toppings = toppings


    def add_topping(self):
        while True:
            topping = input(f"Type 'done' to exit Choose toppings: {toppings_list1} ").lower()

            if topping.lower() == "done":
                break
                
            if topping.lower() not in toppings_lists:
                print("Not a topping")
            else:
                self.toppings.append(topping)
                print(f"Added {topping}")
            
        

    def add_size(self):
        self.size = input("Choose size: ( Small | Medium | Large )")
        
    def add_crust_type(self):
        self.crust_type = input("Choose crust type ( Thin | Medium | Large ): ")

    def remove_topping(self,):
        if not self.toppings:
            print("No toppings to remove.")
            return
        
        removed_topping = input(f"Remove topping from {self.toppings}")


        if removed_topping in self.toppings:
            self.toppings.remove(removed_topping)
            print(f"Removed {removed_topping}")
        else:
            print(f"{removed_topping} is not on your pizza.")


    def pizza_details(self):
        print("---- Your Pizza ----")
        print(f"""Pizza size: {self.size.title()}
Crust type: {self.crust_type.title()}
toppings: {self.toppings}""")
order = Pizza()
order.add_crust_type()
order.add_size()
order.add_topping()
order.remove_topping()
order.pizza_details()
