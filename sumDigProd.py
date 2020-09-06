def mult_digits(integer):
    tmp = str(integer)
    product = 1
    for i in tmp:
        product *= int(i)
    if (len(str(product)) == 1):
        return product
    else:
        return mult_digits(product)
           
    


def sum_digits(lstDigits):
    """
        takes integers as arguments,
        adds them together,
        and returns the product of digits until the
        answer is only 1 digit long.
        inputs:
            lstDigits - string of integers seperated by a single space
        outputs:
            1 digit sum of products
    """
    integers = lstDigits.split(" ")
    total_sum = 0
    for i in integers:
        total_sum += int(i)

    return mult_digits(total_sum)

"""
    Proofs of concept
    print (sum_digits("14 22"))
    print (sum_digits("0"))
    print (sum_digits("1 2 3 4 5 6"))
"""

running = True
while running:
    data = input("Please enter as many integers as you would like seperated by spaces. \nex. 1 2 3\n")
    print ("Your result is " + str(sum_digits(data)))
    again = input("Do you want to do another? Y/n \n")
    if again.lower() =="n":
        running = False
           

