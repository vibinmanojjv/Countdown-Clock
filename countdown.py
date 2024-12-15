import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        print(f"\rTime left: {minutes:02}:{sec:02}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!")
try:
    user_input = int(input("Enter the countdown time in seconds: "))
    if user_input <= 0:
        raise ValueError("Time must be a positive integer.")
    countdown_timer(user_input)
except ValueError as e:
    print(f"Invalid input: {e}")
