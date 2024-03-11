# Перше завдання


from datetime import datetime

date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

def get_days_from_today(date):
    date_formated = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    get_days_from_today = current_date.toordinal() - date_formated.toordinal()
    return int(get_days_from_today)

try:
     print(f"кількість днів між заданою датою {date} і поточною датою  складає {get_days_from_today(date)}")

except ValueError:
    print(f"помилка формату дати {date}")

