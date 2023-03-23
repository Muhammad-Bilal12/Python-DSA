# ptn -> 1
'''
    * * * *
    * * * *
    * * * *
    * * * *
'''
# CODE

# n = int(input("number "))

# for row in range(0, n):
#     for col in range(0, n):
#         print('* ', end="") # for print
#     print() # for line break


"""
    1 1 1
    2 2 2
    3 3 3
"""

# n = int(input("number "))

# for row in range(1, n+1):
#     for col in range(0, n):
#         print(row, end="")  # for print
#     print()  # for line break

# for reverse loops
# for i in range(5,0,-1):
#     print(i)


#######################################################################
# Kunal Kushwasha Series Start

""" - pattern 2-
* 
* *
* * *
* * * *
* * * * *
"""


def pattern2(n):
    # Run outer loop for number of line your pattern have
    for row in range(1, n+1):  # outer loop
        # run inner loop to identify the columns
        for col in range(1, row+1):
            print("* ", end="")
        print()  # fot printing new line

# --------------------------------------------------


'''
    * * * * * 
    * * * *
    * * *
    * *
    *
'''


def pattern3(n):
    # Run outer loop for number of line your pattern have
    # for row in range(n, 0,-1):  # outer loop
    #     # run inner loop to identify the columns
    #     for col in range(row, 0, -1):
    #         print("* ", end="")
    #     print()  # fot printing new line

    # another approch
    for row in range(1, n+1):  # outer loop
        # run inner loop to identify the columns
        for col in range(0, n-row+1):
            print("* ", end="")
        print()  # fot printing new line


# --------------------------------------------------

'''
    1  
    1  2
    1  2  3
    1  2  3  4
'''


def pattern4(n):
    #    Run outer loop for number  of line your pattern have
    for row in range(1, n+1):  # outer loop
        # run inner loop to identify the columns
        for col in range(1, row + 1):
            print(col, " ", end="")
        print()  # fot printing new line

# --------------------------------------------------


'''
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * * 
    *
'''


def pattern5(n):
    #    Run outer loop for number  of line your pattern have
    for row in range(0, 2*n):  # outer loop
        # run inner loop to identify the columns
        totalcolinrows = 2 * n - row if (row > n) else row
        for col in range(0, totalcolinrows):
            print("* ", end="")
        print()  # fot printing new line


# --------------------------------------------------
# Diamond Question

'''
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''


def pattern6(n):
    #    Run outer loop for number  of line your pattern have
    for row in range(0, 2*n):  # outer loop
        # run inner loop to identify the columns
        totalcolinrows = 2 * n - row if (row > n) else row

        noofspaces = n - totalcolinrows
        for space in range(0, noofspaces):
            print(" ", end="")
        for col in range(0, totalcolinrows):
            print("* ", end="")
        print()  # fot printing new line


# --------------------------------------------------
'''
    1
   212
  32123
 4321234
543212345
'''


def pattern6(n):
    #    Run outer loop for number  of line your pattern have
    for row in range(1, n+1):  # outer loop
        # run inner loop to identify the columns

        # for print spaces
        for space in range(0, n - row):
            print(" ", end="")

        # for print left col value
        for col in range(row, 0, -1):
            print(col, end="")

        # for print left col value
        for col in range(2, row + 1):
            print(col, end="")
        print()  # fot printing new line

# --------------------------------------------------


'''
    1
   212
  32123
 4321234
543212345
 4321234
  32123
   212
    1
'''


def pattern7(n):
    #    Run outer loop for number  of line your pattern have
    for row in range(1, 2*n):  # outer loop
        # run inner loop to identify the columns

        totalcolinrows = 2 * n - row if (row > n) else row

        # for print spaces
        for space in range(0, n - totalcolinrows):
            print(" ", end="")

        # for print left col value
        for col in range(totalcolinrows, 0, -1):
            print(col, end="")

        # for print left col value
        for col in range(2, totalcolinrows + 1):
            print(col, end="")
        print()  # fot printing new line


# --------------------------------------------------

'''
444444444
433333334
432222234
432111234
432101234
432111234
432222234
433333334
444444444

'''


def pattern8(n):
    # most outer loop
    orignal_n = n
    n = 2*n
    for row in range(1, n+1):
        # inner loop
        for col in range(0, n+1):
            at_every_index = orignal_n - \
                min(min(row, col), min(n-row, n-col)) if orignal_n != 0 else 1
            print(at_every_index, end="")
        print()


# ---------------------------- Code Execution
n = int(input("Enter Number: "))
pattern8(n)
