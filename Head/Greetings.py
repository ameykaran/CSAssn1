from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def morning():
    print("Hello! Good morning")


def afternoon():
    print("Hello! Good afternoon")


def evening():
    print("Hello! Good evening")


def night():
    print("Hello! Good night")


if "00:00:00" <= current_time < "05:00:00":
    night()

elif "05:00:00" <= current_time < "12:00:00":
    morning()

elif "12:00:00" <= current_time < "16:00:00":
    afternoon()

elif "16:00:00" <= current_time < '20:00:00':
    evening()

elif "20:00:00" <= current_time <= "23:59:59":
    night()
