def check_year(year):
    if year == '1799':
        return(True)
    else:
        return(False)

year = input('Ввведите год рождения А.С.Пушкина:')
while not check_year(year):
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')
print('Верно')

def check_day(day):
    if day == '6':
        return(True)
    else:
        return(False)

day = input('В какой день июня родился Пушкин?')
while not check_day(day):
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')