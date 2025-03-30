from email.headerregistry import Group

from multiprocessing.reduction import duplicate
#Задача 7.1
numbers =[5,16,24,48,100]
user_num = int(input("Введите число: "))
print(f"Исходный список: {numbers}")
print(f"Ваше число: {user_num}")
if user_num in numbers:
    print("Поздравляю, Вы угадали число")
else:
    print("Нет такого числа")

#Задача 7.2
my_list=[1,5,3,5,7,2,3]
print(f"Исходный список: {my_list}")
duplicates = set([x for x in my_list if my_list.count(x)> 1])
if duplicates:
    print(f"Повторяющиеся элементы: {duplicates}")
else:
    print(f"Повторяющихся элементов нет")

#Задача 7.3
days = ("Понедельник", "Вторник,", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
weekends_count = int(input("Сколько выходных дней вы хотите на неделе?"))
weekends = list(days[-weekends_count:])
workdays = list(days[:-weekends_count])
print(f"Ваши выходные дни: {weekends}")
print(f"Ваши рабочие дни: {workdays}")

#Задание 7.4
group1 =["Иванов", "Смирнов","Сидоров","Пузиков","Емельянов","Шаповалов","Васильв","Соколов","Петров","Клещёв"]
group2 =["Кузнецов","Мамедов","Ивков","Шатов","Боков","Янковский","Корнеев","Агеев","Дараган","Целуйко"]
sport_team = tuple(group1[:5] + group2[:5])
print(f"Группа 1: {group1}")
print(f"Группа 2: {group2}")
print(f"Спортивная Команта: {sport_team}")
print(f"Длинна команды: {len(sport_team)}")
sorted_team = tuple(sorted(sport_team))
print(f"Отсортированная команда: {sorted_team}")
ivanov_count = sport_team.count("Иванов")
if ivanov_count > 0:
    print(f"Студент Иванов входит в команду, встречается {ivanov_count} раз(а)")
else:
    print("Студент Иванов не входит в команду")