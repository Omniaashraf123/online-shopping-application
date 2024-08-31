#online shopping application
from inventory import inventory,add_product_inventory, update_product_inventory,remove_product_inventory,display_inventory
from cart import cart,add_cart, view_cart, remove_from_cart
from order import place_order


def display_menu():
    print("\n  Online Shopping App ")
    print("1.Browse product")
    print("2.View Cart")
    print("3.Place Order")
    print("4. Exit")


def get_choice():
       return input("enter your choice: ")



def main():
    #main  of app
    
    while True:
       display_menu()
       choice = get_choice()


       try: 
           if choice == '1':
                #allow user to browse avaliable product
               display_inventory()
               prod_id = input("enter product id to add to cart: ")
               quantity = int(input("enter quantity: "))
               if quantity <= 0:
                  raise ValueError("quantity must be positive integar ")
               add_cart(prod_id, quantity)

 
           elif choice == '2':
                 view_cart()
                 prod_id = input("enter product id to remove from cart (or press enter to skip): ")
                 if prod_id:
                    remove_from_cart(prod_id)

           elif choice == '3':
            place_order()

           elif choice == '4':
            print("Thank You for your purchase ")
            break

           else:
             print("invalid choice. please try again")

       except ValueError as e:
           print(f"Error: {e}")
       except Exception as e: 
           print(f"unexpected error happen: {e}")


if __name__ == "__main__":
    main()
               















