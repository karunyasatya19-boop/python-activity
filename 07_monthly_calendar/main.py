print("MONTHLY CALENDAR GENERATOR")
try:
    days = int(input("Enter number of days in the month (28-31): "))
    start = int(input("Starting weekday (0=Sun, 1=Mon, ..., 6=Sat): "))
    if days < 28 or days > 31 or start < 0 or start > 6:
        print("Invalid month length or starting weekday.")
    else:
        print("Sun Mon Tue Wed Thu Fri Sat")
        print("    " * start, end="")
        for date in range(1, days + 1):
            print(f"{date:3} ", end="")
            if (start + date) % 7 == 0:
                print()
        print()
except ValueError:
    print("Please enter whole numbers only.")
