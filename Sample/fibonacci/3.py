while True:  # keep asking until valid input is given
    try:  # catch non-integer input
        n = int(input("Enter n: "))  # read input and convert to integer
        if n < 0:  # reject negative numbers
            print("n must be 0 or greater.")  # tell the user what's wrong
            continue  # ask again
        break  # valid input, exit the loop
    except ValueError:  # input wasn't a whole number
        print("Please enter a whole number.")  # tell the user what's wrong

a, b = 0, 1  # first two Fibonacci numbers
while a <= n:  # continue while current term is within n
    print(a, end=" ")  # print current term on the same line
    a, b = b, a + b  # move to the next pair in the series

print()
