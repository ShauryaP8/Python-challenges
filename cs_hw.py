import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time -= 1
    print("Time Finished")

def allocate_screen_time():
    num_siblings = int(input("Number of sibilings: "))
    total_time = int(input("Enter total screentime: "))
    if num_siblings > 0:
        indiviual_time = total_time // num_siblings
        print(f"Each sibiling gets {indiviual_time}")

        for i in range(1, num_siblings + 1):
            print(f"\nSibling {i}, your screen time starts")
            countdown(indiviual_time * 60)
            print(f"Sibiling {i} yu time is up")
    else:
        print("num of siblings should at least be 1")

allocate_screen_time()