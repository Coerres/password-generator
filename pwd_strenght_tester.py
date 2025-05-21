import string
import re
import math

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "admin", "letmein", "welcome", "monkey", "dragon", "football", "iloveyou"
}

def estimate_entropy(pw):
    pool = 0
    if any(c.islower() for c in pw): pool += 26
    if any(c.isupper() for c in pw): pool += 26
    if any(c.isdigit() for c in pw): pool += 10
    if any(c in string.punctuation for c in pw): pool += len(string.punctuation)
    return round(len(pw) * math.log2(pool)) if pool and len(pw) > 0 else 0

def print_bar(score):
    bar_length = 30
    filled = int(score / 100 * bar_length)
    print("[" + "#" * filled + "-" * (bar_length - filled) + "]")

def password_strength(password: str) -> int:
    score = 0
    length = len(password)
    feedback = []

    # Length scoring (up to 32)
    if length >= 8:
        score += min(length, 64) * 0.5
    else:
        score -= (8 - length) * 2
        feedback.append("Password is too short (minimum 8 characters recommended).")

    # Character variety
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    types = [has_lower, has_upper, has_digit, has_special]

    score += types.count(True) * 10  # Max 40

    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_digit:
        feedback.append("Add digits.")
    if not has_special:
        feedback.append("Add special characters (e.g., !, @, #, etc).")

    if all(types):
        score += 10  # Bonus

    # Entropy (max +10)
    entropy = estimate_entropy(password)
    if entropy > 60:
        score += 10
    elif entropy < 30:
        feedback.append("Password entropy is low. Try using more randomness.")

    # Pattern and repetition penalties
    if re.search(r'(.)\1{3,}', password):
        score -= 10
        feedback.append("Avoid repeated characters like 'aaa' or '111'.")

    if re.search(r'(0123|1234|2345|abcd|qwer|asdf)', password.lower()):
        score -= 10
        feedback.append("Avoid using common keyboard patterns or sequences.")

    if password.lower() in COMMON_PASSWORDS:
        score -= 25
        feedback.append("Avoid using very common passwords.")

    # Normalize
    score = max(0, min(int(score), 100))

    # Strength label
    if score < 30:
        label = "Very Weak"
    elif score < 50:
        label = "Weak"
    elif score < 70:
        label = "Moderate"
    elif score < 90:
        label = "Strong"
    else:
        label = "Very Strong"

    print(f"\nPassword strength: {label} ({score}/100)")
    print_bar(score)

    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print(f"- {f}")
    else:
        print("Your password looks great!")

    return score

def password_strength_setup():
    while True:
        print("\nPassword Strength Tester")
        print("========================")
        password = input("Enter a password to test its strength (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Exiting Password Strength Tester. Goodbye!")
            break
        password_strength(password)

if __name__ == "__main__":
    password_strength_setup()
