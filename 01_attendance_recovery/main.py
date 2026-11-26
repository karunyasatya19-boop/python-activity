def attendance_recovery(total_classes, attended_classes, target):
    if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
        return None
    if target <= 0 or target > 100:
        return None

    current = attended_classes / total_classes * 100
    extra = 0
    while (attended_classes + extra) / (total_classes + extra) * 100 < target:
        extra += 1
    final = (attended_classes + extra) / (total_classes + extra) * 100
    return current, extra, final

print("ATTENDANCE RECOVERY CALCULATOR")
try:
    total = int(input("Enter total classes held: "))
    attended = int(input("Enter classes attended: "))
    target = float(input("Enter required attendance percentage: "))
    result = attendance_recovery(total, attended, target)
    if result is None:
        print("Invalid input. Check the number of classes and target percentage.")
    else:
        current, extra, final = result
        print(f"Current attendance: {current:.2f}%")
        print("Additional consecutive classes to attend:", extra)
        print(f"Attendance after attending them: {final:.2f}%")
except ValueError:
    print("Please enter valid numeric values.")
