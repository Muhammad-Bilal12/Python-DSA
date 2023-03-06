# If Condition

# Using following list of cities per country,

# 1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
# 2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
#  "They don't belong to same country


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

user_city = input("Enter Your City: ")
# print(user_city)
if user_city in india:
    print(f"{user_city} is in india")
elif user_city in pakistan:
    print(f"{user_city} is in Pakistan")
elif user_city in bangladesh:
    print(f"{user_city} is in Bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

city1 = input("Enter city 1:") 
city2 = input("Enter city 2:")

if city1 in india and city2 in india:
    print("Both Citise are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both Citise are in Pakistan")

elif city1 in bangladesh and city2 in bangladesh:
    print("Both Citise are in Bangladesh")
else:
    print("They don't belong to same country")
