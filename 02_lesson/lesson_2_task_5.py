def month_to_season(n):
    if 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "лето"
    elif 9 <= n <= 11:
        return "Осень"
    else:
        return "Зима"


n = int(input("Введите номер месяца (1-12): "))
print(month_to_season(n))
