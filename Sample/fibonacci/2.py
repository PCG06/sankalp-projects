while True:
    try:
        n = int(input("Enter n: "))
        if n < 0:
            print("n must be 0 or greater.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b

print()
