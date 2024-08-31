#dictionary to represent product inventory

inventory = {
    "001": {'name': 'T-shirt', 'price': 450, 'quantity': 50},
    "002": {'name': 'Jeans', 'price': 600, 'quantity': 30}
}

def add_product_inventory(prod_id, name, price, quantity):
    #add new product to inventory

    if prod_id in inventory:
         print("product id already exist in inventory")
    else:
        inventory[prod_id] = {'name': name, 'price': price, 'quantity': quantity}


def update_product_inventory(prod_id, name=None, price=None, quantity=None):
    #update details of exist product in inventory
    if prod_id in inventory:
            if name:
                inventory[prod_id]['name'] = name
            if price:
                inventory[prod_id]['price'] = price
            if quantity is not None:
                inventory[prod_id]['quantity'] = quantity
            else:
                 print("product not found")


def remove_product_inventory(prod_id):
    #remove product from inventory
    if prod_id in inventory:
        del inventory[prod_id]
    else:
        print("product not found")

def display_inventory():
    # Display all products in the inventory
    print("\nAvailable Products:")
    for prod_id, product in inventory.items():
        print(f"iD: {prod_id}, name: {product['name']}, price: EGP {product['price']}, quantity: {product['quantity']}")