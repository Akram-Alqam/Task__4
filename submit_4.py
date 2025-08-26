prices = {"apple" : 0.5, "banana" : 0.3, "orange" : 0.6, "mango" : 1.2, "strawberry" : 0.25}
fruits = input("Enter a fruit name: ").lower()
if fruits in prices:
    print(f"the price of {fruits} is ${prices[fruits]:.2f}")
else:
    print("Sorry, this fruit is not available.")