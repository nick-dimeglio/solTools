import requests


# THIS IS THE THIRD STEP OF THE PROGRAM.
# This takes the tokens from the salesInformation function and checks their recent sales via magiceden API.
def saleCheck(tokens):
    # establishing the sale array to hold all the tokens' sales to be sorted
    sales = []
    for token in tokens:
        # Using magic eden API to get each token's sale history to a max of 5 recent transactions
        url = f'https://api-mainnet.magiceden.dev/v2/tokens/{token}/activities?offset=0&limit=5'
        response = requests.get(url).json()
        # Looping through the 5 recent transactions to see if they are a sale and appending sales to the sale array.
        for item in response:
            if item['type'] == 'buyNow':
                sales.append(item)
    # Sorting the sales array by block as highest block means more recently processed on the blockchain.
    sales = sorted(sales, key=lambda k: k['slot'])
    # Looping through the sorted sales array to print out the most recent sale history of each token sorted by block (time).
    for sale in sales:
        print(
            f'NFT with token: {sale["tokenMint"]} sold during block: {sale["slot"]} for: {sale["price"]} SOL')

# SECOND STEP IN PROGRAM
# Takes collection queried by user in the first step, and returns a list of all the desired tokens in the collection.


def salesInformation(collection):
    # Establishing arrays for all the items in the entire colleciton, the names of all the attributes, and the eventual tokens that fit the query of the user.
    itemsInCollection = []
    # not currently using the attribute categories, but its easily acccessible here if ever needed.
   # attributeNames = []
    attributeValues = []
    desiredTokens = []
    # Using howrare.is to get the entire collection of items in the desired collection.
    url = f'https://api.howrare.is/v0.1/collections/{collection}'
    response = requests.get(url).json()
    # Filtering json to just get the items in the collection.
    validityCheck = response['result']
    if validityCheck['api_code'] == 200:
        fullList = response['result']['data']['items']
        # Looping through all the individual NFTs in the collection and each of their attributes to check for all possible attributes and adding them to the value array.
        for item in fullList:
            for attribute in item['attributes']:
                #  if attribute['name'] not in attributeNames:
                #     attributeNames.append(attribute['name'])
                if str(attribute['value']).lower() not in attributeValues:
                    attributeValues.append(str(attribute['value']).lower())
        # After successfully grabbing all possible valid attributes, asking user which they'd like to see the sales history of.
        print("What attribute would you like to see the sales history of?")
        # Gotta make sure its lowercase for simplicity!
        desiredAttribute = str(input("Attribute: ").lower())
        # A simple way to check if the user's input is among the valid attributes. If its not, just loop 'em through to choose again.
        while desiredAttribute not in attributeValues:
            if desiredAttribute in attributeValues:
                break
            print('That attribute does not exist in this collection. Please try another.')
            desiredAttribute = str(input("Attribute: ").lower())
        # Once a valid attribute is chosen, loop through each NFT and its attribute once more to see if the NFT has the desired attribute
        # If it does, add the token of the NFT to the desiredToken array.
        for item in fullList:
            for attribute in item['attributes']:
                if str(attribute['value']).lower() == desiredAttribute:
                    desiredTokens.append(item['mint'])\
                        # Once all the matches are found, send them to the saleCheck function to have their recent sale information checked.
        print("NFT Tokens found. Finding recent sales history of all tokens. This may take a while depending on how many tokens grabbed and how steady MagicEden is at the moment...")
        saleCheck(desiredTokens)
    else:
        print('There was an error grabbing this collection. Please make sure it was spelled correctly and try again.')
        salesHistory()

# FIRST STEP IN PROGRAM
# Asks user for which collection they want to see the sales history of.


def salesHistory(collection=None):
    # Check if being redirected back from the salesInformation function from invalid input.
    if collection is not None:
        salesInformation(collection)
    # This is the usual intro where the collection is asked for and the query is sent off to the salesInformation function.
    else:
        print("What collection would you like to see the sales history of?")
        collection = str(input("Collection: ").lower())
        print(
            "One second while the collection and all of its attributes are being loaded...")
        salesInformation(collection)
