#!/usr/bin/env python
# coding: utf-8

# ## Restaurant Billing System

# In[22]:


import datetime

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "French Fries": 100,
    "Cold Coffee": 80,
    "Ice Cream": 90,
    "Biryani": 250
}

def show_menu():
    """Display menu items with prices."""
    print("\n------ MENU CARD ------")
    for item, price in menu.items():
        print(f"{item} : ₹{price}")
    print("------------------------")

def take_order():
    """Take customer order and return a dictionary of items."""
    order = {}
    while True:
        item = input("\nEnter item name (or 'done' to finish order): ").title().strip()
        if item.lower() == "done":
            break
            
        if item not in menu:
            print("Item not available, choose from the menu.")
            continue

        qty = input(f"Enter quantity for {item}: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Quantity should be a positive number.")
            continue

        order[item] = order.get(item, 0) + int(qty)
        print(f"Added {qty} {item} to your order.")
    return order

def calculate_bill(order):
    """Calculate subtotal, GST, discount, and total for an order."""
    subtotal = sum(menu[item] * qty for item, qty in order.items())
    gst = subtotal * 0.05
    discount = subtotal * 0.10 if subtotal >= 300 else 0
    total = subtotal + gst - discount
    return subtotal, gst, discount, total

def generate_bill_number():
    """Generate a unique bill ID using current date and time."""
    return datetime.datetime.now().strftime("R%Y%m%d%H%M%S")

def save_order(order):
    """Save the full order to file."""
    with open("orders.txt", "a", encoding="utf-8") as file:
        file.write(str(order) + "\n")

def view_saved_orders():
    """Display all previously saved orders."""
    try:
        with open("orders.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if content.strip():
                print("\n======= PREVIOUS ORDERS =======\n")
                print(content)
            else:
                print("No previous orders found.")
    except FileNotFoundError:
        print("No order file found yet.")

def display_bill(bill_no, order_items, subtotal, gst, discount, total):
    """Display the bill"""
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("\n========= BILL =========")
    print(f"Bill Number : {bill_no}")
    print(f"Date & Time : {date_time}")
    print("------------------------------")
    print(f"{'Item':15}{'Qty':<5}{'Price':<7}{'Total'}")
    print("------------------------------")
    for item, qty in order_items.items():
        price = menu[item]
        total_price = price * qty
        print(f"{item:15}{qty:<5}{price:<7}{total_price}")
    print("------------------------------")
    print(f"Subtotal : ₹{subtotal}")
    print(f"GST      : ₹{gst:.2f}")
    print(f"Discount : ₹{discount:.2f}")
    print(f"TOTAL    : ₹{total:.2f}")
    print("==============================\n")

def add_review(order):
    """Ask customer to provide rating, feedback, and suggestions."""
    rating_options = {
        1: "Very Bad",
        2: "Bad",
        3: "Good",
        4: "Very Good",
        5: "Excellent"
    }

    give_review = input("Would you like to give a rating, feedback, and suggestions? (yes/no): ").lower().strip()
    if give_review == 'yes':
        while True:
            print("\nRate your experience:")
            for key, value in rating_options.items():
                print(f"{key} – {value}")
            rating = input("Enter your rating (1-5): ")
            if rating.isdigit() and 1 <= int(rating) <= 5:
                rating = int(rating)
                break
            else:
                print("Please enter a valid number between 1 and 5.")
        
        feedback = input("Share your feedback about food/service: ").strip()
        
        suggestions = input("Any suggestions for improvement? (optional): ").strip()
    else:
        rating = None
        feedback = None
        suggestions = None

    order['rating'] = f"{rating} – {rating_options[rating]}" if rating else None
    order['feedback'] = feedback
    order['suggestions'] = suggestions

def run_restaurant():
    """Main function to control the flow"""
    while True:
        print("\n====== Restaurant Billing ======")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. View Previous Orders")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            order = take_order()
            if not order:
                print("No items selected.")
                continue

            bill_no = generate_bill_number()
            subtotal, gst, discount, total = calculate_bill(order)

            order = {
                'id': bill_no,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'items': order,
                'subtotal': subtotal,
                'gst': round(gst, 2),
                'discount': round(discount, 2),
                'total': round(total, 2)
            }

            display_bill(bill_no, order['items'], subtotal, gst, discount, total)
            add_review(order)
            save_order(order)
            print("Thank you. Visit again")

        elif choice == "3":
            view_saved_orders()

        elif choice == "4":
            print("Exit")
            break

        else:
            print("Invalid choice. Please select 1-4.")


run_restaurant()


# In[ ]:





# In[ ]:




