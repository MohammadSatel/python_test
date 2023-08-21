import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown_time = int(input("Enter the countdown time in seconds: "))
countdown_timer(countdown_time)

if __name__== '__main__':
    print("restarting")
