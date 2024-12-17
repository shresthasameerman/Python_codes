def main():
    # Dictionary to store countries and their capitals
    country_capitals = {}

    while True:
        # Prompt the user to enter a country name
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()

        # Check if the user wants to exit
        if country.lower() == 'exit':
            print("Exiting the program.")
            break

        # Normalize the country name to handle case insensitivity
        normalized_country = country.lower()

        # Check if the capital is already known
        if normalized_country in country_capitals:
            print(f"The capital of {country} is {country_capitals[normalized_country]}.")
        else:
            # Ask the user to enter the capital city
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            # Store the country and its capital in the dictionary
            country_capitals[normalized_country] = capital
            print(f"Thank you! The capital of {country} has been recorded as {capital}.")

if __name__ == "__main__":
    main()