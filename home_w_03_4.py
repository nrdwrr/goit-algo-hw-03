
# Четверте завдання

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1992.03.15"},
    {"name": "John Slow", "birthday": "1985.03.23"},
    {"name": "Mary Fox", "birthday": "1991.04.11"},
    {"name": "John Smither", "birthday": "1992.03.17"}
]




def find_next_weekday(d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    """
     Ф-ція для знаходження наступного заданого дня тижня після заданої дати
    :param d: datetime.date - початкова дата
    :param weekday: int - день тижня від 0 (понеділок) до 6 (неділя)
    :return:
    """
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату




def get_upcoming_birthdays(users):
    today = datetime.today().date()  # Поточна дата
    days = 7  # Кількість днів для перевірки на наближені дні народження
    prepared_users = []  # Список підготовлених користувачів

    for user in users:  # Ітерація по кожному користувачеві зі списку
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  # Парсимо дату народження
            prepared_users.append({"name": user['name'], 'birthday': birthday})  # Додаємо користувача з підготовленою датою народження

        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  # Виводимо повідомлення про помилку
    
    lucky_oners = []  # Список майбутніх днів народження
    for user in prepared_users:  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року
        if birthday_this_year < today:  # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= days:  # Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # Знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            lucky_oners.append({  # Додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return lucky_oners


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

