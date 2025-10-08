def Fuel_Efficiency_Calculator(km, fuel):
    Fuel_Efficiency = km / fuel
    print("Fuel Efficiency:", round(Fuel_Efficiency, 2), "km/L")
    
km = float(input("Enter distance traveled (in kilometers):"))
fuel = float(input("Enter fuel consumed (in liters):"))

Fuel_Efficiency_Calculator(km, fuel)