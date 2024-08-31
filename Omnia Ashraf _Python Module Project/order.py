# importing the random module to make random number for order id
import random
from cart import cart,add_cart, view_cart, remove_from_cart

def calculate_total():
    #calculate total amount for order
    return sum(item['subtotal'] for item in cart.values())


def place_order():
    #place order and display order summary

    if not cart:
        print("cart is empty")
        return False
    
    total = calculate_total()
    order_id = f"ORD{random.randint(1000, 9999)}"
    print(f"\nOrder ID: {order_id}")
    print("\nOrder Summary: ")
    for prod_id, item in cart.items():
        print(f"ID: {prod_id}, name: {item['name']}, quantity: {item['quantity']}, subtotal: EGP {item['subtotal']}")
    print(f"Total: EGP {total}")    
    cart.clear()
    
    return True