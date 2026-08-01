

SENTINEL = "quit"   # the "Kill Switch" -- typing this ends the session


def get_expense():
    """
    The Gatekeeper: ask for one piece of input and safely convert it.
    Returns a float for a valid expense, the sentinel string to stop,
    or None if the input was invalid (so the caller can retry).
    """
    raw = input(f"Enter an expense amount (or '{SENTINEL}' to finish): ").strip()

    if raw.lower() == SENTINEL:
        return SENTINEL

    try:
        # int('100') + int('50') = 150 (Truth), NOT '100' + '50' = '10050'
        amount = float(raw)
    except ValueError:
        print("⚠️  Invalid input. Please enter a number (e.g. 100 or 49.99).\n")
        return None

    if amount < 0:
        print("⚠️  Expenses can't be negative. Try again.\n")
        return None

    return amount


def track_expenses():
    """
    The Accumulator: run the continuous audit loop, adding every
    valid expense to the running total.
    """
    total = 0.0          # state initialized OUTSIDE the loop -- this
    count = 0             # is what makes it "memory" instead of "amnesia"
    expenses = []          # keeps a record for the receipt at the end

    print("===== DecodeLabs Expense Tracker =====\n")

    while True:                       # the continuous audit loop
        expense = get_expense()

        if expense == SENTINEL:
            break                      # graceful shutdown via sentinel value
        if expense is None:
            continue                   # bad input -- don't touch the total

        total += expense               # the accumulator pattern in action
        count += 1
        expenses.append(expense)
        print(f"✅ Added ${expense:.2f}  |  Running total: ${total:.2f}\n")

    return total, count, expenses


def show_summary(total, count, expenses):
    """OUTPUT layer: decoupled from the logic that computed it."""
    print("\n----- EXPENSE SUMMARY -----")
    if count == 0:
        print("No expenses were recorded.")
    else:
        for i, amount in enumerate(expenses, start=1):
            print(f"{i}. ${amount:.2f}")
        average = total / count
        print("----------------------------")
        print(f"Transactions : {count}")
        print(f"Total Spent  : ${total:.2f}")
        print(f"Average      : ${average:.2f}")
    print("----------------------------\n")


def main():
    total, count, expenses = track_expenses()
    show_summary(total, count, expenses)


# The gatekeeper pattern -- only runs when executed directly.
if __name__ == "__main__":
    main()
