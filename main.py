# Importing all the other tools as they are held in separate files for readability.
import floorprice as fp
# Not necessary yet to import unused feature
#import pricehistory as ph

# This is the main hub for the program. It will show the user the available tools and ask for which tool they would like to use once its run
# At the moment, the input is run through if else statements, but this will be swapped as grows
# The only way to close the program/while loop is for the user to input "exit".


def main():
    print("Welcome to solTools!")
    print("Available tools: floorprice")
    print("Type 'exit' to quit.")
    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        elif command == "floorprice":
            fp.floor()
        # I will add this in the near future, I'd rather there be a constantly updated firebase database for this though. I'll have a use for this soon!
        # elif command == "pricehistory":
            # ph.price_history()
        else:
            print("Invalid command. Please enter one of the available tools.")


main()
