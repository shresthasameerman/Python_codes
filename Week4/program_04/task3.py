def greet_user():
    # Prompt the user to enter their name
    name = input("Please enter your name: ")
    
    # Capitalize the name
    formatted_name = name.capitalize()
    
    # Display the greeting
    print(f"Hello, {formatted_name}!")

# Call the function to greet the user
greet_user()