print("FOOD WASTE MONITORING SYSTEM")
try:
    days = int(input("Enter number of days to record: "))
    limit = float(input("Enter acceptable waste limit percentage: "))
    if days <= 0 or limit < 0 or limit > 100:
        print("Enter a positive number of days and a limit from 0 to 100.")
    else:
        records = []
        for i in range(days):
            day = input(f"Enter day {i+1} name: ")
            prepared = int(input("Meals prepared: "))
            served = int(input("Meals served: "))
            while prepared <= 0 or served < 0 or served > prepared:
                print("Invalid values: prepared must be positive and served cannot exceed prepared.")
                prepared = int(input("Meals prepared: "))
                served = int(input("Meals served: "))
            records.append((day, prepared, served))
        print("\nFOOD WASTE REPORT")
        total_prepared = total_served = total_leftover = 0
        for day, prepared, served in records:
            leftover = prepared - served
            waste = leftover / prepared * 100
            total_prepared += prepared
            total_served += served
            total_leftover += leftover
            print(f"{day}: Prepared={prepared}, Served={served}, Leftovers={leftover}, Waste={waste:.2f}%")
            if waste > limit:
                print("  HIGH WASTE: exceeds the set limit")
        overall = total_leftover / total_prepared * 100
        print("\nTOTAL PREPARED:", total_prepared)
        print("TOTAL SERVED:", total_served)
        print("TOTAL LEFTOVERS:", total_leftover)
        print(f"OVERALL WASTE: {overall:.2f}%")
except ValueError:
    print("Please enter valid numeric values.")
