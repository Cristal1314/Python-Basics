#booleans
print(10 > 9)#is this ture or false?
#  booleans are used to evaluate expressinos and conditions in python
#  they are used to check it an expression is ture or false
broughtFood = True
print(broughtFood)
is_raining = True
if is_raining: 
    print("Take an umbrella")

else:
    print("No umbrella needed.")


temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
    print("Done")

age = 22
if age >= 18:
    message = " Eligible"
else:
    message = "Not eligible"


message = "Eligible" if age >= 18 else "Not eligible"
print(message)