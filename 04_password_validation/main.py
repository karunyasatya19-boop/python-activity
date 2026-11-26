def validate_password(password):
    has_upper = has_lower = has_digit = has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    errors = []
    if len(password) < 8:
        errors.append("Use at least 8 characters")
    if not has_upper:
        errors.append("Add at least one uppercase letter")
    if not has_lower:
        errors.append("Add at least one lowercase letter")
    if not has_digit:
        errors.append("Add at least one digit")
    if not has_special:
        errors.append("Add at least one special character")
    return errors

print("PASSWORD POLICY VALIDATOR")
password = input("Enter a password to check: ")
problems = validate_password(password)
if not problems:
    print("Password is valid and meets all rules.")
else:
    print("Password is invalid:")
    for problem in problems:
        print("-", problem)
