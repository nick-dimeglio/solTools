import requests
import os
from genericpath import exists
import time

# This function will be called below in floorprice_check to log the floor price and its timestamp
# to a separate file that will be accessed in pricehistory.py each time that you check the floorprice
# of a collection.


def floorprice_logger(collection, floorprice):
    file = open("floorprice_log.txt", "a")
    file.write(collection)
    file.write(" " + str(floorprice) + " " + str(int(time.time())))
    file.write("\n")
    file.close()


# Defining a function to check the floor price of a collection.

def floorprice_check(collection):
    # define the url for the stats page of a collection using the Magic Eden API.
    url = f'https://api-mainnet.magiceden.dev/v2/collections/{collection}/stats'
    # Get the response by requesting the URL.
    response = requests.get(url)
    # Check if the collection is valid by seeing if there is a floorprice in the response.
    # If there is, grab the floor price from the response, divide it by 10^9 (to get the price in full SOL), and return it.
    # Also run the floorprice_logger function as stated above (currently on hold because I want to flesh out the usefulness of this feature).
    if 'floorPrice' in response.json():
        floorprice = response.json()['floorPrice']
        floorprice = floorprice / 1000000000
        #floorprice_logger(collection, floorprice)

        return(floorprice)
    else:
        return(f"No floor price found. {collection} likely doesn't exist on Magic Eden. If you are positive it does, try again later as Magic Eden may be offline.")


# Main function for using the floorprice tool. Takes the user through dialogue to get the collection name and check the floor price.

def floor():
    # Check if there was a previous search (as if there was, a file will be created)
    if exists('floorprice.txt'):
        # If the file does exist, ask the user if they would like to search the same floor prices.
        print("Would you like to check the floor prices of the collections you previously searched for? (y/n)")
        check_floor_price_history = str(input("(y/n): "))
        # If the user does want to, open the file, read each line of the file (after stripping the spaces just in case),
        # and run the floorprice_check function on each individual line/collection.
        # AND close the file.
        if check_floor_price_history == "y":
            file = open("floorprice.txt", "r")
            for line in file:
                line = line.strip()
                check_floor = floorprice_check(line)
                # If the function returns a float value, it means everything was successful and the user should be shown the floor price.
                # If the function returns a string, it means the collection doesn't exist on Magic Eden or ME API is down, and the user should be shown the error.
                if isinstance(check_floor, float):
                    print(
                        f'The floor price of {line} is currently {check_floor} SOL')
                else:
                    print(check_floor)
            file.close()
        # If the user does not want to, delete the file, and rerun this function as it will skip to the else statement.
        elif check_floor_price_history == "n":
            os.remove("floorprice.txt")
            floor()

        # If the user enters anything else, the user should be shown the error message and the function should be run again.
        else:
            print("Invalid input. Please input either 'y' or 'n'.")
            floor()

    # If the file does not exist, or if they just deleted the file from the previous section, ask the user for comma separated collections they want to search.
    # Then, split the string by commas, and run the floorprice_check function on each individual line/collection.
    # However, to make a sort of cache, a file will be opened/created, and each individual collection will be written to the file via the same for loop separated by lines.
    else:
        print("Please enter a collection name (or collections separated by comma ex: solgods, degods, cets_on_creck).")
        floor_price_collection_name = str(
            input("Collection Name(s) (As seen on Magic Eden URL): "))
        collections = floor_price_collection_name.split(",")
        file = open("floorprice.txt", "w")
        for collection in collections:
            collection = collection.strip()
            file.write(collection)
            file.write("\n")
            check_floor = floorprice_check(collection)
            print(
                f'The floor price of {collection} is currently {check_floor}')
        file.close()
