print("NUMBER PYRAMID GENERATOR")
try:
    rows = int(input("Enter number of rows (1 to 9): "))
    if rows < 1 or rows > 9:
        print("Please enter a number from 1 to 9.")
    else:
        for i in range(1, rows + 1):
            print("  " * (rows - i), end="")
            for number in range(1, i + 1):
                print(number, end=" ")
            print()
except ValueError:
    print("Please enter a whole number.")
