def km_to_miles(km):
    return km * 0.621371

km = float(input("Enter distance in km:"))
print(f"{km} km = {km_to_miles(km):.2f} miles")