import string

def check_password_strength(password):
    # Define criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    digit_weight = 1
    special_char_weight = 2

    # Initialize scores
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    digit_score = 0
    special_char_score = 0

    # Check password length
    if len(password) >= 8:
        length_score = length_weight

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        uppercase_score = uppercase_weight

    # Check for lowercase letters
    if any(char.islower() for char in password):
        lowercase_score = lowercase_weight

    # Check for digits
    if any(char.isdigit() for char in password):
        digit_score = digit_weight

    # Check for special characters
    special_chars = string.punctuation
    if any(char in special_chars for char in password):
        special_char_score = special_char_weight

    # Calculate total score
    total_score = (length_score + uppercase_score + lowercase_score +
                   digit_score + special_char_score)

    # Determine strength level based on total score
    if total_score >= 9:
        strength = "Very Strong"
    elif total_score >= 7:
        strength = "Strong"
    elif total_score >= 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    print(f"Password Strength: {strength}")
    print(f"Total Score: {total_score}")

# Example usage:
def main():
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
