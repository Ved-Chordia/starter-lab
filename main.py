import datetime, bday_messages

today = datetime.date(2025, 4, 12)
next_birthday = datetime.date(2026, 2, 23)
time_difference = next_birthday - today
days_away = time_difference.days

if today == next_birthday:
    print(bday_messages.random_message())
else:
    print(f"My next birthday is {days_away} days away!")
