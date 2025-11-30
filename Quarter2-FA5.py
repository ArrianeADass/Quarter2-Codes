
destinations = []

print("Enter your 5 travel destinations:")
for i in range(5):
    place = input(f"Destination {i+1}: ")
    destinations.append(place)


print("\nYour original travel destinations:")
print(destinations)


new_second = input("\nEnter a NEW destination to replace the 2nd destination: ")
destinations[1] = new_second

new_fifth = input("Enter a NEW destination to replace the 5th destination: ")
destinations[4] = new_fifth  


print("\nYour UPDATED travel destinations:")
for i, place in enumerate(destinations, start=1):
    print(f"{i}. {place}")