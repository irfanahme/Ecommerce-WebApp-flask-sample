# Initial product data: product_id, name, image, rating
products = {
    1001: {"name": "Laptop", "image": "laptop.png", "rating": 4.5},
    1002: {"name": "Smartphone", "image": "smartphone.png", "rating": 4.3},
    1003: {"name": "Tablet", "image": "tablet.png", "rating": 4.2},
}

# Variable to keep track of the next available product ID
next_product_id = max(products.keys()) + 1 if products else 1001

# Function to validate image extension
def isValidImageExtension(image):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    return any(image.lower().endswith(ext) for ext in valid_extensions)

# Function to display all products
def showAllProducts():
    if not products:
        print("\nNo products available.\n")
    else:
        print("\n--- All Products ---")
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Rating: {details['rating']}, Image: {details['image']}")
        print()

# Function to add a new product
def addNewProduct():
    global next_product_id
    print("\n--- Add New Product ---")
    
    name = input("Enter product name: ")
    
    # Image validation loop
    while True:
        image = input("Enter product image filename (must be .jpg, .jpeg, .png, .gif): ")
        if isValidImageExtension(image):
            break
        else:
            print("Invalid image extension! Please enter a valid image file (.jpg, .jpeg, .png, .gif).")
    
    rating = float(input("Enter product rating (0-5): "))
    
    products[next_product_id] = {"name": name, "image": image, "rating": rating}
    print(f"Product '{name}' added successfully with ID {next_product_id}.\n")
    
    next_product_id += 1  # Increment the product ID for the next addition

# Function to delete a product
def deleteProduct():
    if not products:
        print("\nNo products available to delete.\n")
    else:
        print("\n--- Delete Product ---")
        # First, show all products
        showAllProducts()
        
        # Ask for the product ID to delete
        product_id = int(input("Enter product ID to delete: "))
        
        if product_id in products:
            del products[product_id]
            print(f"Product with ID {product_id} deleted successfully.\n")
        else:
            print("Product ID not found.\n")

# Function to update product rating
def updateProductRating():
    print("\n--- Update Product Rating ---")
    product_id = int(input("Enter product ID to update rating: "))
    
    if product_id in products:
        new_rating = float(input("Enter new product rating (0-5): "))
        products[product_id]['rating'] = new_rating
        print(f"Rating for product ID {product_id} updated to {new_rating}.\n")
    else:
        print("Product ID not found.\n")

# Main function to handle menu and user input
def mainMenu():
    while True:
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        choice = input("Enter Option to continue: ")

        if choice == '1':
            showAllProducts()
        elif choice == '2':
            addNewProduct()
        elif choice == '3':
            deleteProduct()
        elif choice == '4':
            updateProductRating()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Call the main menu to start the application
if _name_ == "_main_":
    mainMenu()