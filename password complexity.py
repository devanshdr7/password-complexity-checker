import re

def check_password_strength(password):
    strength = 0
    feedback = []


    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")


    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")


    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")


    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")


    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")


    if strength <= 2:
        result = "Weak Password"
    elif strength == 3 or strength == 4:
        result = "Medium Strength"
    else:
        result = "Strong Password"

    return result, feedback


password = input("Enter your password: ")
strength_result, suggestions = check_password_strength(password)

print(f"\nResult: {strength_result}")

if suggestions:
    print("Suggestions to improve your password:")
    for tip in suggestions:
        print(f" - {tip}")
else:
    print("Great! Your password is strong.")
