def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about; what its responsibilities are;
    what the parameters are
    what datatypes 

    Example of invoking the function: 
    to_usd(9.999)
    """
    return '${:,.2f}'.format(my_price)



##if this code is in the global scope of a file we're trying to import from:
##it will throw errors when we try to run those other files 
#price = input("Please choose a price, like 4.999:")
#print(to_usd(float(price)))



if __name__ == "__main__":
    #if this code is in the global scope of a file we're trying to import from:
    # it will throw errors when we try to run those other files 
    price = input("Please choose a price, like 4.999:")
    print(to_usd(float(price)))



#we want the global scope to be clean 
#nesting code in the main condition will allow other scripts to cleanly import functions from this file
#main conditional can still run the whole utilities file 

#def determine_winner(u,c):
    """
    """
    #gamewinner = winner[u][c]

    #return 