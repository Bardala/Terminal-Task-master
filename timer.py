import time
import re
import threading
import signal
import sys


class Timer:
    def __init__(self, t):
        self.t = self.parse_time(t)
        self.stop_event = threading.Event()

    def parse_time(self, t):
        hours = re.search(r"(\d+)h", t)
        minutes = re.search(r"(\d+)m", t)
        seconds = re.search(r"(\d+)s", t)
        total_seconds = 0
        if hours:
            total_seconds += int(hours.group(1)) * 3600
        if minutes:
            total_seconds += int(minutes.group(1)) * 60
        if seconds:
            total_seconds += int(seconds.group(1))
        return total_seconds

    def countdown(self):
        while self.t and not self.stop_event.is_set():
            mins, secs = divmod(self.t, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.t -= 1
        print("Timer completed!")

    def stop(self):
        self.stop_event.set()


timer_input = input("Enter time: ")
timer = Timer(timer_input)

# Start the countdown in a new thread
thread = threading.Thread(target=timer.countdown)
thread.start()


# def signal_handler(sig, frame):
#     threading.Event().is_set()
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)


# The rest of your program can continue here while the timer runs in the background
user_input = input("\nenter input: ")
print(user_input)
