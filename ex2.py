import math

'''Exercise: Numbers in python
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
Print binary representation of number 17'''


# Q1
length = 92 
wide = 48.8
area = length * wide
# print(area)
# print(round(area,2))

# ------------------------------------------- #

# Q2
buy_item = 9
cost = 1.49
total_amount = buy_item*cost
# print("total amount: ",total_amount)
pay = 20
cash_back = pay - total_amount
# print("cash_back: ",cash_back)

# Q3
cost_of_tiles_sq_feet = 500
area_of_tiles = 5.5**2
# print("Area of Tiles: ",area_of_tiles)
total_cost = (area_of_tiles*cost_of_tiles_sq_feet)
# print("Total cost to replace the tiles is RS: ",total_cost)


# Q4
# print(dir(17))
num = 17
print("binary representation of 17 is: ",format(num,'b'))
