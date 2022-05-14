# solTools

Tools for the solana network, at the moment mostly revolving around the Magic Eden marketplace.

# Currently Available

At the moment, the currently usable functions within this build are:

-   ### Floorprice Check:
    -   Check as many floor prices separated by commas at once
    -   Automatically save the previous search, so all you don't need to keep entering the same collections.
-   ### Sales History Check:
    -   Check the sales history of a collection based on a certain trait.
    -   Support for every NFT collection available on howrare.is
    -   Can support up to 120 NFTs within a trait.

# Additions Planned

For the future, I want to add a few features that would help potential buyers a bit more closely:

-   Price History
-   Volume Notifications
-   Discord Bot Integration for constant updates
-   Firebase/Database integration for centralized data of the collections.
-   Add staggering to API queries to get around 120 TPM limit of MagicEden.

# How To Use

### Step One:

Be sure to have python installed.

### Step Two:

Download this repo whether its via a zip file or by cloning. If you use the zip file, just be sure to extract it to it's own folder.

### Step Three:

Download any libraries used via pip.

Currently required libraries:
-   #### Requests

This can be done via terminal by using the command (without quotations):
"pip install requests"

If you have issues with this, you can use:
"py -m pip install requests"

### Step Four:

You are going to need to have a terminal window up, and depending on which you are using you will execute a semi-different command.

#### Using VS Code built-in terminal:

"py main.py"

#### Using CMD prompt or other dedicated terminal:

-   Open CMD prompt or whatever terminal you are using for your operating system, and navigate to the folder that contains the python files. For instance if you have it installed in your C: drive downloads folder, your command prompt should look something like this:

![image](https://user-images.githubusercontent.com/73611619/168404935-ec02d4c4-b0d1-4719-8364-b32ac49c58bc.png)

-   After you've navigated into this folder within your terminal, simply run the command (without quotations):

"py main.py"

### Step Five:

Use the program!
From here, you can select from the available tools by simply typing in the name of the tool you want to use.
No matter what you choose, the program should prompt you on how to format inputting commands and queries.

Here's a quick example of it working and the functionality:

Floorprice:

![image](https://user-images.githubusercontent.com/73611619/168405012-40de21c8-7951-4937-945c-ab3fa3aa1237.png)

SalesHistory:

![image](https://user-images.githubusercontent.com/73611619/168448969-b73ca57e-73de-4ddf-b095-14796c7ea5b6.png)

I hope you find this tool useful in your Solana NFT endeavours!
