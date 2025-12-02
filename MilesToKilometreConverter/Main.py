# Conversions
def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

# User Input
while True:
    print("1- miles to KM")
    print("2- KM to miles")
    print("0- exit")

    choice = input("Chose an option: ")

    if choice == "1":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")
    elif choice == "2":
        km = float(input("Enter km: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == "0":
        break
    else:
        print("Invalid option.")
