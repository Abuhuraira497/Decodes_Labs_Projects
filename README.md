# Decodes_Labs_Projects
# Python Programming — Industrial Training KitDecodeLabs | Batch 2026

This repository contains my submissions for the DecodeLabs Python Industrial Training Kit. Each project builds on the last, moving from basic data storage to real-time data processing — the foundational skills behind any backend engineering system.

#	Project	Core Skill	Status
1	To-Do List	Lists (append, loops, enumerate())	✅ Complete
2	Expense Tracker	Math operations & the Accumulator Pattern	✅ Complete
3	Random Password Generator	Module imports (secrets, string) & string manipulation	✅ Complete
Project 1 — To-Do List

File: todo_list.py

Overview

A command-line task manager where a user can add tasks, view them, mark them as done, and delete them. It demonstrates how to store multiple related items in a single Python list, the same primitive idea that later scales up into database tables.

Features
Add tasks to a list (list.append())
View all tasks with numbering via enumerate() (instead of manual range(len(...)) indexing)
Mark tasks as done (✔ status flag)
Delete tasks by number
Persistence — tasks are saved to tasks.json on disk, so the list survives after the program closes (moving data from volatile RAM to permanent storage)
Input validation for empty entries and invalid menu/task selections
How to Run
bash
python3 todo_list.py

Follow the on-screen menu (1–5) to add, view, complete, delete, or exit.

Sample Output
===== DecodeLabs To-Do List =====
1. Add a task
2. View tasks
3. Mark a task as done
4. Delete a task
5. Exit
Choose an option (1-5): 2

----- YOUR TO-DO LIST -----
[ ] 1. Finish Python assignment
[✔] 2. Walk dog
----------------------------
Project 2 — Expense Tracker

File: expense_tracker.py

Overview

A command-line tool that continuously accepts expense amounts from the user, adds them together in real time, and displays a final itemized summary. It demonstrates the Accumulator Pattern (total += new_expense) — the core logic behind ledgers, backend calculations, and any system that maintains a running state.

Features
Continuous input loop (while True) that keeps accepting expenses until the user is done
Accumulator pattern: total is initialized outside the loop so it correctly builds up state instead of resetting each pass
Defensive coding: invalid (non-numeric) or negative input is rejected with a clear message, without corrupting the running total
Sentinel value (quit) as a graceful "kill switch" to end the session
Final summary showing every transaction, the total spent, and the average expense
How to Run
bash
python3 expense_tracker.py

Enter expense amounts one at a time. Type quit when finished to see the summary.

Sample Output
Enter an expense amount (or 'quit' to finish): 100
✅ Added $100.00  |  Running total: $100.00

Enter an expense amount (or 'quit' to finish): 50
✅ Added $50.00  |  Running total: $150.00

Enter an expense amount (or 'quit' to finish): quit

----- EXPENSE SUMMARY -----
1. $100.00
2. $50.00
----------------------------
Transactions : 2
Total Spent  : $150.00
Average      : $75.00
----------------------------
Project 3 — Random Password Generator

File: password_generator.py

Overview

A command-line tool that generates cryptographically secure, random passwords of a user-specified length. It demonstrates how to import and combine Python's built-in secrets and string modules to solve a real security problem, rather than hand-rolling character logic or reaching for the (insecure) random module.

Features
Cryptographically secure randomness — uses secrets.choice() and a manual secrets-based Fisher-Yates shuffle throughout, never random, since random is built on the predictable Mersenne Twister and is unfit for anything security-related
Standardized character pools via the string module (ascii_lowercase, ascii_uppercase, digits, punctuation) instead of manually typed character arrays
Guaranteed complexity — every password includes at least one lowercase letter, one uppercase letter, one digit, and (optionally) one symbol, with positions shuffled securely so they aren't predictable
Efficient string building — characters are collected in a list and joined once with ''.join() (O(N)), avoiding the O(N²) cost of repeatedly doing password += char on Python's immutable strings
NIST SP 800-63-4 (2024) aware validation — enforces an 8-character minimum and advises 15+ characters for high-security use
Entropy reporting — calculates password strength using E = L × log2(R) and displays a strength rating (Weak / Moderate / Strong / Very strong)
Optional inclusion/exclusion of special symbols, and the ability to generate multiple passwords per session
How to Run
bash
python3 password_generator.py

Enter your desired password length, choose whether to include symbols, and repeat as needed.

Sample Output
Enter desired password length (minimum 8): 20
Include special symbols? (Y/n): n

----- GENERATED PASSWORD -----
gew9LUPJkHNrFo6HwUnc
-------------------------------
Length      : 20 characters
Entropy     : 119.1 bits
Strength    : Very strong
-------------------------------
Repository Structure
.
├── todo_list.py           # Project 1: To-Do List
├── expense_tracker.py     # Project 2: Expense Tracker
├── password_generator.py  # Project 3: Random Password Generator
├── tasks.json              # Auto-generated by Project 1 (task storage)
└── README.md               # This file
Requirements
Python 3.7+ (Project 3 requires 3.6+ for the secrets module)
No external libraries required (uses only the standard library: json, os, secrets, string, math)
Author

Abuhruraira BS Artificial Intelligence Intern, DecodeLabs — Batch 2026

Acknowledgment

Built as part of the DecodeLabs Python Programming Industrial Training Kit, designed to build hands-on backend engineering fundamentals through incremental, real-world-style projects.
