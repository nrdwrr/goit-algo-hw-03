# Перше завдання


from datetime import datetime

def get_days_from_today(date):
        
    try:

        date_formated = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        get_days_from_today = current_date.toordinal() - date_formated.toordinal()
        return int(get_days_from_today)

    except ValueError:

        return(f"некоректні вхідні дані: {date}. спробуйте ще")

       

date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")


print(f"кількість днів між заданою датою {date} і поточною датою  складає: {get_days_from_today(date)}")


