#topping_lists has it's own function to caclualate the price
toppings_list1 = "pepperoni, sausage, mushrooms, onions, bell peppers, black olives, extra cheese, ham, pineapple, bacon, chicken"
crust_type = {"Thin": 1.00, "Medium" : 1.50, "Large" : 1.99, "Deep Dish" : 2.49}
size_list = {"Small" : 6.50, "Medium" : 9.50, "Large" : 10.00}
answers = ["yes", "y"]
toppings_lists = toppings_list1.split(", ")
price = 0
wallet = 100.00

def calculate_tax(price):
    result = price * .06
    return result

def calculate_price(size, crust, toppings=1):
    individual_topping = 0.60

    individual_prices = []
    base_price = size_list[size] + crust_type[crust]
    for i in range(1, toppings+1):
        individual_topping += (i * 0.08)
        individual_prices.append(round(individual_topping, 2))
        base_price = base_price + individual_topping
    return base_price, individual_prices

class Pizza:

        def __init__(self, size="", crust_type="", toppings=None):
            self.size = size
            self.crust_type = crust_type
            if toppings is None:
                self.toppings = []
            else:
                self.toppings = toppings
            #allows a user to add a topping in the list of toppings
            #remember to make it a dictionary of prices somehow
        def add_topping(self):
            print(f"Available toppings: {toppings_list1} ")
            while True:
                
                topping = input(f"Type topping name to add topping or 'done' to finish. ").lower().strip()

                if topping == "done":
                    return
                    
                if topping in toppings_lists:
                    self.toppings.append(topping)
                    print(f"Added {topping}.")
                else:
                    print("Not a valid topping.")

            #add_size function allows a user to add a size in the given list.
        def add_size(self):
            while True:
                choice = input(f"Choose size {size_list}: ").title().strip()
                if choice in size_list:
                    self.size = choice      
                    return
                print("Not a valid size")
            #add_crust_type function allows a user to add a crust type in the given list.
        def add_crust_type(self):
            while True:
                choice = input(f"Choose crust {crust_type}: ").title().strip()
                if choice in crust_type:
                    self.crust_type = choice
                    return
                print("Not a valid crust type")
            
              # remove_topping function allows a user to remove a topping if the pizza has a topping.
              # Additionally, if there are no toppings left or user types 'exit', they will leave this method/function.
        def remove_topping(self):
            if not self.toppings:
                print("No toppings to remove.")
                return
            while True:
                print(f"Current toppings: {', '.join(self.toppings)}")
                removed_topping = input(f"Type ingredient name to remove. Type 'done' to exit.: ").lower().strip()
                if removed_topping in self.toppings:
                    self.toppings.remove(removed_topping)
                    print(f"Removed {removed_topping}")
                
                else:
                    print(f"{removed_topping} is not on your pizza.")
                if removed_topping == "done":
                    return
                if not self.toppings:
                    return
        # Prints a user's pizza details including tax and taxxed amount
        # Add itemized list price
        def pizza_details(self):
            price, topping_price = calculate_price(self.size, self.crust_type, len(self.toppings))
            tax_amount = calculate_tax(price)
            
            pizza_crust = f"{self.crust_type} ${crust_type[self.crust_type]}"
            pizza_size = f"{self.size} ${size_list[self.size]}"
       
            print("---- Your Pizza ----")
            print(f"Size: {pizza_size}")
            print(f"Crust: {pizza_crust}")
            print(f"Toppings: ")
            if not self.toppings:
                print(f" - Regular Cheese: ${price}")
            else:
                for i in range(0, len(self.toppings)):
                    name = self.toppings[i]
                    value = topping_price[i]
                    print(f" - {name} ${value:.2f}")

            print(f"{"Subtotal".capitalize()}: {price:.2f}")
            print(f"Sales Tax: ${tax_amount:.2f}")
            print(f"Total Price: ${(price + tax_amount):.2f}")
            print("--------------------")

order = Pizza()
order.add_crust_type()
order.add_size()
order.add_topping()
if order.toppings:
    remove_t = input("Do you want to remove a topping? type ('Y/N'): ").lower().strip()
    if remove_t in answers:
        order.remove_topping()

order.pizza_details()
