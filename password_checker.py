common_passwords = [
    "password",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123"
]
def check_length(password):
    return len(password) >= 8


def check_uppercase(password):
    return any(i.isupper() for i in password)


def check_lowercase(password):
    return any(i.islower() for i in password)


def check_digit(password):
    return any(i.isdigit() for i in password)

def check_special(password):
    return any(i in "@#$%&*!?_" for i in password)


def check_space(password):
    return " " in password


def main():
    while True:
        print("\n========== PASSWORD STRENGTH CHECKER ==========")

        password = input("Enter password: ")

        if password == "":
            print("Password cannot be empty")
            continue
        if password.lower() in common_passwords:
           print("Weak password: This is a commonly used password.")
           continue

        length_valid = check_length(password)
        uppercase_valid = check_uppercase(password)
        lowercase_valid = check_lowercase(password)
        digit_valid = check_digit(password)
        special_valid = check_special(password)
        space_found = check_space(password)

        if space_found:
            print("Invalid password: Spaces are not allowed")
            continue

        print("\nPassword Analysis")
        print("Length:", "Passed" if length_valid else "Failed")
        print("Uppercase:", "Passed" if uppercase_valid else "Failed")
        print("Lowercase:", "Passed" if lowercase_valid else "Failed")
        print("Digit:", "Passed" if digit_valid else "Failed")
        print("Special character:", "Passed" if special_valid else "Failed")
        print("--------------------------------")

        score = length_valid + uppercase_valid + lowercase_valid + digit_valid + special_valid

        print(f"Password Score: {score}/5")
        print("=" * 10, "PASSWORD STRENGTH", "=" * 10)

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Moderate"
        else:
            strength = "Strong"

        print(f"Your password is: {strength}")
        print("=" * 40)
        if not length_valid:
            print("Suggestion: Password should contain at least 8 characters.")

        if not uppercase_valid:
            print("Suggestion: Add at least one uppercase letter.")

        if not lowercase_valid:
            print("Suggestion: Add at least one lowercase letter.")

        if not digit_valid:
            print("Suggestion: Add at least one digit.")

        if not special_valid:
            print("Suggestion: Include at least one special character.")

        choice = input("\nCheck another password? (yes/no): ")

        if choice.lower() != "yes":
            print("Thank you for using Password Strength Checker!")
            break


main()