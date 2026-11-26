print("WEEKLY ELECTRICITY CONSUMPTION ANALYSIS")
try:
    count = int(input("Enter number of appliances: "))
    if count <= 0:
        print("Enter at least one appliance.")
    else:
        appliances = []
        readings = []
        for i in range(count):
            name = input(f"Enter appliance {i+1} name: ")
            appliances.append(name)
            row = []
            print(f"Enter daily kWh usage for {name} (7 days):")
            for day in range(7):
                value = float(input(f"Day {day+1}: "))
                while value < 0:
                    print("Usage cannot be negative.")
                    value = float(input(f"Day {day+1}: "))
                row.append(value)
            readings.append(row)
        totals = []
        print("\nWEEKLY APPLIANCE TOTALS")
        for i in range(count):
            total = sum(readings[i])
            totals.append(total)
            print(appliances[i], ":", round(total, 2), "kWh")
        print("\nDAILY TOTALS")
        for day in range(7):
            daily = sum(readings[i][day] for i in range(count))
            print("Day", day+1, ":", round(daily, 2), "kWh")
        highest = totals.index(max(totals))
        print("\nHighest consumption:", appliances[highest], round(totals[highest], 2), "kWh")
except ValueError:
    print("Please enter valid numeric values.")
