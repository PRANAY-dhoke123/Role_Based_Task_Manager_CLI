def safe_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print(f"Please enter a valid number. ERROR {ValueError} Try again.\n")