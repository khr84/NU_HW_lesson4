
def check_answer(question, date):
    answer = input(question)
    while answer != date:
        print('Не верно')
        answer = input(question)

check_answer('Ввведите год рождения А.С.Пушкина: ','1799')
print('Верно')
check_answer('Ввведите день рождения Пушкина: ','6')
print('Верно')