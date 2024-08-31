# online-shopping-application
This Python-based application is a basic online shopping system where users can browse products, add items to their cart, place orders, and manage product inventory. The application uses a modular approach, ensuring that the code is easy to maintain and extend.

## Features
- **Product Inventory Management:**
- Add, update, and remove products from the inventory.
- View available products with details such as ID, name, price, and quantity.
  
- **User Interface and Input Handling:**
- Menu-driven interface for easy navigation.
- Input validation to ensure data integrity.
  
- **Product Browsing and Cart Management:**
- Browse products and add items to your shopping cart.
- View, update, or remove items from the cart.
  
- **Order Placement and Summary:**
- Place orders and generate a summary with total cost.
- Clear the cart after a successful order placement.
  
- **Error Handling:**
- Handle invalid inputs, out-of-stock products, and other potential errors gracefully.
  
## How to Run the Application
### Prerequisites
- Python 3.12.5 must be installed on your system.
  
### Steps to Run
1. **Download the Script:**
- Clone the repository or download the `onlineshopping.py` file.
  
2. **Run the Application:**
- Open a terminal or command prompt.
- Navigate to the directory where the script is located.
- Execute the script by running:

```bash
python onlineshopping.py
```
- Follow the prompts displayed in the terminal to interact with the application.
  
### Example Commands
- **Add a Product to Inventory:**
- Use the menu option to add a new product, providing its ID, name, price, and quantity.
  
- **Browse Products:**
- View the list of available products, including details like name, price, and stock quantity.
  
- **Add Items to Cart:**
- Select products and specify quantities to add them to your shopping cart.
  
- **Place an Order:**
- Review your cart and place an order. The application will generate a summary of your purchase.
  
### Exiting the Application
- To exit the application, select the "Exit" option from the main menu.
  
## Assumptions
- Product IDs are unique and non-repetitive.
- The user provides valid data types when prompted.
- The application is run in a terminal or command-line environment.
  
## Future Enhancements
- Implementing a database for persistent product and order storage.
- Adding a graphical user interface (GUI).
- Introducing user authentication for a more secure experience.
  
## Test Cases
### 1. Adding Products to Inventory
- **Scenario:** Add new products and verify they are stored correctly.
- **Steps:**
1. Add a product with ID `001`, name `T-shirt`, price `EGP 450`, and quantity `50`.
2. Add another product with ID `002`, name `Jeans`, price `EGP 600`, and quantity `30`.
- **Expected Outcome:** Both products are successfully added and displayed in the inventory.
  
### 2. Browsing Products
- **Scenario:** View available products.
- **Steps:**
1. Use the menu option to browse products.
2. Check if the details of each product are displayed correctly.
- **Expected Outcome:** All products in the inventory are listed with correct details.
  
### 3. Adding Items to Cart
- **Scenario:** Add items to the cart and verify contents.
- **Steps:**
1. Add multiple items to the cart from the product list.
2. View the cart to ensure the correct items and quantities are added.
- **Expected Outcome:** The cart displays all selected items with the correct quantities.
  
### 4. Placing an Order
- **Scenario:** Place an order
