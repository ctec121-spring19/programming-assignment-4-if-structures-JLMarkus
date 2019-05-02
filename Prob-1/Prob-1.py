# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Jason Markus

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    # enter code here to test for free
    if (orderSubTotal >= 10.00):
        shippingCost = 0
    else:
        shippingCost = 2.99

    return shippingCost

def unitTest(subtotal):
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(subtotal))
    # enter additional test code here
    print("Your subtotal is", subtotal)

if __name__ == "__main__":
    unitTest(9.99)
