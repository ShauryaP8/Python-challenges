def guess_the_number():
    low = 1
    high = 111

    while low <= high:
        mid = (low + high) // 2
        response= input(f"IS the number {mid}? (Enter 'higher', 'lower', or 'correct'): ")

        if response == "higher":
            low = mid + 1
        elif response == "lower":
            high = mid - 1
        elif response == "correct":
            print(f"Number found: {mid}")
            return
        else:
            print("Please enter a valid Resoponse")

    print("I could not find your number...")

guess_the_number()
