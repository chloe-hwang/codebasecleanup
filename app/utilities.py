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


#mainconditional

if __name__ == "__main__":
    #if this code is in the global scope of a file we're trying to import from:
    # it will throw errors when we try to run those other files 
    price = input("Please choose a price, like 4.999:")
    print(to_usd(float(price)))


