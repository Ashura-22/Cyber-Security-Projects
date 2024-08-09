import re  # Regex import

print("<-------------------Password Complexity Checker------------------->")
print("To make password complex, it should contain:\n1. Lowercase Letter.\n2. Uppercase Letter\n3. Numbers\n4. Special Characters\n5. Password Length should be >= 8")

password = input("\nEnter Password: ")  # input

# Regex pattern explanation:
# ^                 : Start of string
# (?=.*[a-z])       : At least one lowercase letter
# (?=.*[A-Z])       : At least one uppercase letter
# (?=.*\\d)         : At least one digit
# (?=.*[-+_!@#$%^&*.,?]) : At least one special character
# .{8,}             : Minimum length of 8 characters
# $                 : End of string

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%^&*.,?]).{8,}$"
res = re.match(pattern, password)

if res:
    print("\nThe entered password '" + password + "' is complex and can't be cracked easily.")
else:
    print("\nThe entered password '" + password + "' is not complex and can be cracked easily!")

#print(password)