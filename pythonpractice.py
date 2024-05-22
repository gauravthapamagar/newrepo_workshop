# Configurable variables
STUDENT_DISCOUNT_PERCENTAGE = 0.10
HST_PERCENTAGE = 0.13
DELIVERY_CHARGE = 5
TIP_CHOICES = [10, 15, 20]

def welcome_screen():
    print("Welcome to Arnold's Amazing Eats!")
    print("------------------------------------")
    print("The program is designed to inform about the ordering process for delicious food delivery in Waterloo.")
    print("You can place your order by contacting our staff member via call or text.")
    print("We promise you to bring the best meals delivered right to your door.")
    print("Thank you for choosing Arnold's Amazing Eats!")
    print("-------------------------------------------------\n")

def studentconfirmation():
    while True:
        student_status = input("Are you a student? (Y/N): ").strip().lower()
        if student_status in ["y", "n"]:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    if student_status == "y":
        print(f"A student discount of {STUDENT_DISCOUNT_PERCENTAGE * 100}% is applied on your purchase.")
        return STUDENT_DISCOUNT_PERCENTAGE
    else:
        return 0

def customerdetails():
    prompts = {
        "first_name": "Please Enter your first name:",
        "last_name": "Please Enter your last name:",
        "street_number": "Please Enter the street number:",
        "street_name": "Please Enter the street name:",
        "unit": "Please Enter your unit number(if applicable):",
        "city": "Please Enter your city:",
        "province": "Please Enter your province:",
        "postal_code": "Please Enter postal code:",
        "delivery_instructions": "Please provide any special deliveries instructions (if possible):",
        "phone_no": "Please enter your phone number:",
        "pickup_or_delivery": "Is your order for pickup or delivery? (P/D): "
    }

    customer_info = {}
    for key, prompt in prompts.items():
        value = input(prompt).strip()
        if key == "pickup_or_delivery":
            while value.lower() not in ["p", "d"]:
                print("Invalid input. Please enter 'P' for pickup or 'D' for delivery.")
                value = input(prompt).strip()
        customer_info[key] = value

    return customer_info

def calculate_total_cost_with_hst(totalcost_after_discount):
    # Applying HST (Harmonized Sales Tax)
    totalcost_with_hst = totalcost_after_discount * (1 + HST_PERCENTAGE)
    return totalcost_with_hst

def order_dinner(customer_info, menu):
    def select_meal():
        print("\nPlease select a dinner item:")
        for key, value in menu.items():
            print(f"{key}. {value['name']} ${value['price']}")
        while True:
            select_item = input("\nEnter the meal you wish to buy for the dinner (1 to 6): ").strip()
            if select_item in menu.keys():
                return select_item
            else:
                print("Invalid input. Please select a valid meal.")

    def confirm_order():
        while True:
            confirmation = input("Is this order correct? (Y/N): ").strip().lower()
            if confirmation in ["y", "n"]:
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        return confirmation

    def print_receipt(select_item, meals_ordered, totalcost_before_discount, customer_info, discount_percentage):
        tip_amount = 0
        print("\nReceipt:")
        print("\nCustomer Information:")
        print("Name:", customer_info["first_name"] + " " + customer_info["last_name"])
        print("Phone Number:", customer_info["phone_no"])

        # Display pickup/delivery information
        pickup_or_delivery = customer_info.get("pickup_or_delivery", "").strip().lower()
        delivery_charge = 0
        if pickup_or_delivery == "d":
            print("Address:", customer_info["street_number"] + " " + customer_info["street_name"] + " " + customer_info["unit"])
            print("City, Province, Postal Code:", customer_info["city"] + ", " + customer_info["province"] + ", " + customer_info["postal_code"])
            print("Delivery Instructions:", customer_info["delivery_instructions"])

            # Calculate delivery charge
            delivery_charge = DELIVERY_CHARGE
            total_cost_before_hst = totalcost_before_discount - (totalcost_before_discount * discount_percentage)
            if total_cost_before_hst >= 30:
                print("Delivery Charge: Waived")
                delivery_charge = 0
            else:
                print(f"Delivery Charge: ${delivery_charge:.2f}")
                
            # Ask for tip percentage
            while True:
                tip_percentage = input(f"Would you like to tip the delivery person? Enter {', '.join(map(str, TIP_CHOICES))} (percentage): ")
                if tip_percentage.isdigit() and int(tip_percentage) in TIP_CHOICES:
                    break
                else:
                    print("Invalid input. Please enter one of the specified tip choices.")
        
            tip_amount = total_cost_before_hst * (int(tip_percentage) / 100)
            print(f"Tip: {tip_percentage}% (${tip_amount:.2f})")

        elif pickup_or_delivery == "p":
            print("Order Type: Pickup")

        print()  # Add a blank line

        print("Order".ljust(20) + "Item".ljust(15) + "Item".ljust(15))
        print(" ".ljust(20) + "Amt".ljust(15) + "Price".ljust(15) + "Total".ljust(15))
        print("-" * 10 + "          " + "-" * 4 + "           " + "-" * 5 + "          " + "-" * 6)

        # Printing the selected item dynamically
        for key, value in menu.items():
            if select_item == key:
                print(f"{value['name']}: ".ljust(20) + str(meals_ordered).ljust(15) + f"${value['price']:.2f}".ljust(15) + f"${totalcost_before_discount:.2f}".ljust(15))
                break

        student_savings = totalcost_before_discount * discount_percentage
        subtotal = totalcost_before_discount - student_savings
        tax_amount = subtotal * HST_PERCENTAGE
        total_cost_with_hst = subtotal + tax_amount + tip_amount

        print("\n" + f"{STUDENT_DISCOUNT_PERCENTAGE * 100}% student savings".ljust(50) + f"-${student_savings:.2f}".ljust(15))
        print("Sub Total".rjust(40) + "          "+f"${subtotal:.2f}".ljust(20))
        print("Tax (13%)".rjust(40) + "          "+ f"${tax_amount:.2f}".ljust(20))
        print("Delivery Charge".rjust(40) + "          "+f"${delivery_charge:.2f}".ljust(20))
        if pickup_or_delivery == "d":
            print("Tip".rjust(40) + "          "+f"${tip_amount:.2f}".ljust(20))
        print(" " * 10 + "          " + " " * 4 + "           " + " " * 5 + "          " + "-" * 6)
        print("TOTAL".rjust(40)  + "          "+f"${total_cost_with_hst + delivery_charge:.2f}".ljust(20))


    

    select_item = select_meal()

    meal = menu[select_item]
    meals_ordered = int(input(f"How many {meal['name']} would you like to purchase?: "))
    print(f"You have selected {meals_ordered} {meal['name']} for your dinner")
    confirmation = confirm_order()
    if confirmation == "n":
        print("\n*******\n\nPlease go through the ordering process again to make any necessary changes...")
        order_dinner(customer_info, menu)
        return

    discount_percentage = studentconfirmation()
    totalcost_before_discount = meal['price'] * meals_ordered
    totalcost_after_discount = totalcost_before_discount * (1 - discount_percentage)
    totalcost_with_hst = calculate_total_cost_with_hst(totalcost_after_discount)

    print_receipt(select_item, meals_ordered, totalcost_before_discount, customer_info, discount_percentage)

# Main section
menu = {
    "1": {"name": "Chicken Momo", "price": 6},
    "2": {"name": "Veg Burger", "price": 5},
    "3": {"name": "Pizza", "price": 8},
    "4": {"name": "Pasta", "price": 10},
    "5": {"name": "Sushi", "price": 12},
    "6": {"name": "Salad", "price": 7}
}
welcome_screen()
customer_info = customerdetails()
order_dinner(customer_info, menu)

