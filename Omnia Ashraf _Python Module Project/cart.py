from inventory import inventory,add_product_inventory, update_product_inventory,remove_product_inventory,display_inventory

cart = {}

def add_cart(prod_id, quantity):
    #add product to shopping cart
    if prod_id in inventory:
        product = inventory[prod_id]
        if product['quantity'] >= quantity:
                if prod_id in cart:
                     cart[prod_id]['quantity'] += quantity
                     cart[prod_id]['subtotal'] += product['price'] * quantity
                else:
                     cart[prod_id] = {'name': product['name'], 'quantity': quantity, 'subtotal': product['price'] * quantity}
                inventory[prod_id]['quantity'] -= quantity
        else:
             print("stock not enough")       
    else:
        print("product not found")

def view_cart():
    #display contents of shopping cart
    if not cart:
        print("\ncart is empty")
    else:
        print("\n your cart: ")
        total = 0
        for prod_id, item in cart.items(): 
            print(f"ID: {prod_id}, name: {item['name']}, quantity: {item['quantity']}, subtotal: {item['subtotal']} ")
            total += item['subtotal']
        print(f"total: EGP {total}")    


def remove_from_cart(prod_id):
     #remove product from cart
     if prod_id in cart:
          inventory[prod_id]['quantity'] += cart[prod_id['quantity']]
          del cart[prod_id]
     else:
          print("product not found")

