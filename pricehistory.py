import time
#be sure to have pip install matplot.lib for this library below
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


#Function responsible for plotting the price history of a collection in an easily viewable format
#All the data is gotten from each time the user checks the floorprice of the collection, so at the moment,
#it is all created and stored locally in floorprice_log.txt

def price_history():
    #Ask user for which collection they would like to see the data of.
    collection = input('Enter collection you\'d like to see the price history of: ')
    #Ask user for the timescale they would like to see the data in and ensure its a valid answer.
    time_scale = input('Would you like to see the price history in minutes, hours, or days?')
    if time_scale == 'minutes':
        time_scale = 60
    elif time_scale == 'hours':
        time_scale = 3600
    elif time_scale == 'days':
        time_scale = 86400
    else:
        print('Invalid time scale. Please try again.')
        return
    file =  open('floorprice_log.txt', 'r')

    x=[]
    y=[]
    xdatetime=[]
    
    times_found = 0

    for line in file:
       if collection == line.split(' ')[0]:
            #define x value and y value as the time and price of the collection and remove the excess characters
            #preventing them from being read as an integer.
            #Only x needs to be an integer as that is what will be used in determining the number of ticks
            #along the x-axis, while y is a float.
            xvalue = int(line.split(' ')[2].replace('\n', ''))
            xvalue_datetime = datetime.utcfromtimestamp(xvalue).strftime('%Y-%m-%d %H:%M:%S')
            yvalue = float(line.split(' ')[1].replace('\n', ''))
            #append the x and y values to the x and y lists as defined above
            x.append(xvalue)
            xdatetime.append(xvalue_datetime)
            y.append(yvalue)
            #Increment the times the collection keyword was found in the file.
            #This is used at the moment to test if the collection is logged within the file before proceeding.
            times_found += 1

    print(x)
    print(xdatetime)

    #If the collection is not found in the file, print an error message.
    if times_found == 0:
        print('Collection not found in log. It may be misspelled or you may have never searched the floor price of this collection.')
        return

    file.close()
    # plotting the points
    plt.plot(xdatetime, y)
 
    # naming the x axis
    plt.xlabel('Time')
    # naming the y axis
    plt.ylabel('Price')
    
    #plt.xticks(range(min(x), max(x)))
    # giving a title to the graph
    plt.title(f'Price History of {collection}')
    
    # function to show the plot on screen  
    plt.show()