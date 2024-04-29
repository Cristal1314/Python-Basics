# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".

weather = input("What it the current weather? (sunny, rainy, cold): ")
print(weather)


# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".

if weather == "sunny":
    print("Wear sunglasses and a hat")

# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
elif weather == "rainy":
    print("Carry an umbrella and wear waterproof boots")

# If the weather is "cold", recommend "wear a warm coat and gloves".
elif weather == "cold": 
    print("Wear a warm coat and gloves")
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.
else:
    print("Input not recongnized")