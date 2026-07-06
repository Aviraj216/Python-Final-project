Expense Calculator

A Python console application for tracking personal monthly expenses. Users can create an account, log in, and record expenses across categories like Rent, Food, Transport, Entertainment, and Other.

Features
- User signup & login with credential validation
- Age verification during signup (18+)
- Add expenses: Rent, Grocery (itemized), Travel, and custom "Other" expenses
- View, update, and delete expense records
- Search accounts by email or check rent payment status
- Monthly summary with budget comparison and category breakdown
- Data automatically saved to and loaded from a text file (no data loss between sessions)

How it works
All data is stored in Python lists of dictionaries:
- `myList` — user accounts (ID, name, email, DOB, budget, password)
- `user_expense_data` — expense records linked to each user

On exit, data is written to `user_data.txt` and reloaded 
automatically the next time the program runs.


## Tech
- Pure Python (no external libraries)
- File I/O for persistent storage
- Input validation with try/except
