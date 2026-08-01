

import math
import secrets
import string

MIN_LENGTH = 8
RECOMMENDED_LENGTH = 15  # NIST 2024 guidance for high-security contexts


# INPUT (the Gatekeeper)

def get_password_length():
    """Ask the user for a password length and validate it."""
    while True:
        raw = input(f"Enter desired password length (minimum {MIN_LENGTH}): ").strip()

        if not raw.isdigit():
            print("⚠️  Please enter a whole number.\n")
            continue

        length = int(raw)
        if length < MIN_LENGTH:
            print(f"⚠️  Length must be at least {MIN_LENGTH} characters.\n")
            continue

        if length < RECOMMENDED_LENGTH:
            print(f"ℹ️  Note: NIST recommends {RECOMMENDED_LENGTH}+ characters "
                  f"for high-security accounts. {length} will still work.\n")

        return length


# PROCESS (the transformation engine)
def generate_password(length, use_symbols=True):
    """
    Build a cryptographically secure random password of the given
    length, guaranteeing at least one lowercase letter, one
    uppercase letter, one digit, and (optionally) one symbol.
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Character pool available for the "free" remaining slots
    pool = lower + upper + digits + (symbols if use_symbols else "")

    # Step 1: guarantee at least one of each required category
    required = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
    ]
    if use_symbols:
        required.append(secrets.choice(symbols))

    # Step 2: fill the rest of the length from the full pool
    remaining_count = length - len(required)
    remaining = [secrets.choice(pool) for _ in range(remaining_count)]

    # Step 3: combine and shuffle securely so the guaranteed
    # characters aren't always in the same positions (predictable
    # position = weaker password). random.shuffle() is NOT secure,
    # so we do a manual Fisher-Yates shuffle using secrets.
    password_chars = required + remaining
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    # Step 4: build the final string with .join() -> O(N), not O(N^2)
    return "".join(password_chars), len(pool)



# OUTPUT (decoupled display / reporting layer)
def calculate_entropy(length, pool_size):
    """E = L * log2(R) -- bits of entropy for the generated password."""
    return length * math.log2(pool_size)


def show_result(password, length, pool_size):
    entropy = calculate_entropy(length, pool_size)
    print("\n----- GENERATED PASSWORD -----")
    print(password)
    print("-------------------------------")
    print(f"Length      : {length} characters")
    print(f"Entropy     : {entropy:.1f} bits")
    strength = (
        "Very strong" if entropy >= 90 else
        "Strong" if entropy >= 60 else
        "Moderate" if entropy >= 40 else
        "Weak"
    )
    print(f"Strength    : {strength}")
    print("-------------------------------\n")


# MAIN / MENU LAYER
def main():
    print("===== DecodeLabs Random Password Generator =====\n")

    while True:
        length = get_password_length()

        symbols_choice = input("Include special symbols? (Y/n): ").strip().lower()
        use_symbols = symbols_choice != "n"

        password, pool_size = generate_password(length, use_symbols)
        show_result(password, length, pool_size)

        again = input("Generate another password? (y/N): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay secure. 🔐")
            break


# The gatekeeper pattern -- only runs when executed directly.
if __name__ == "__main__":
    main()
