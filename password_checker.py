import math
import getpass

def calculate_entropy(password):
    pool = 0
    
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in "!@#$%^&*()_+-:;,.<>?/|" for c in password):
        pool += 32
    
    if pool == 0:
        return 0
    
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

print("Password Strength Checker")

password = getpass.getpass("Enter a password: ")

entropy = calculate_entropy(password)

length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(char in "!@#$%^&*()_+-:;,.<>?/|" for char in password)

if length_ok and has_upper and has_lower and has_number and has_symbol:
	print("Strong password")
else:
	print("Weak password")
	print("Your password should have:")
	if not length_ok:
		print("- At least 8 characters")
	if not has_upper:
		print("- At least one uppercase letter")
	if not has_lower:
		print("- At least one lowercase letter")
	if not has_number:
		print("- At least one number")
	if not has_symbol:
		print("- At least one special symbol (!@#$ etc.)")
        
print("Password Entropy:", entropy, "bits")
input("Press Enter to exit...")
