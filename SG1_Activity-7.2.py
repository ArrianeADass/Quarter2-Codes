def Delivery_Fee_Calculator(dist, rate):
    Delivery_Fee = dist * rate
    print("Total Delivery Fee:", Delivery_Fee)
    
dist = float(input("Enter distance in kilometers:"))
rate = float(input("Enter rate per kilometer:"))

Delivery_Fee_Calculator(dist, rate)