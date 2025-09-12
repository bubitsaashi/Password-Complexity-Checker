import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many rules passed
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    # Feedback
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Moderate ⚠️"
    elif score == 2:
        strength = "Weak ❌"
    else:
        strength = "Very Weak 🚨"

    return strength, {
        "Too short (min 8 chars)": length_error,
        "No digit": digit_error,
        "No uppercase letter": uppercase_error,
        "No lowercase letter": lowercase_error,
        "No special character": symbol_error
    }

# Interactive
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, feedback = check_password_strength(pwd)

    print("\nPassword strength:", strength)
    print("Feedback:")
    for rule, failed in feedback.items():
        if failed:
            print(f" - {rule}")
