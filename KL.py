# user_data = {
#     "name": "Слава",
#     "age": "10",
#     "city": "Краснокаменск",
#     "list_hobby": ["лыжи", "электросамокат", "видеоигры"],
# }
# user_data["city"] = "Красноярск"
# user_data["list_hobby"].append("шахматы")

# print(user_data)

# scores = {"Math": 95,
#           "English": 82,
#           "Code": 100,
# }

# for subgect, points in scores.items():
#     print(f"{subgect}: {points}")
# max_point = 0
# for points in scores.values():
#     if points > max_point:
#         max_point = points
# print(f"Максимальный бал: {points}")


# shop = {
#     "apple": 50,
#     "banana": 30,
#     "cherry": 80,
# }
# sale = {
# }

# for subject, points in shop.items():
#     sale[subject] = points * (80/100)
#     print(f"{subject}: {points}")
    
# print(sale)


# Программа «Успеваемость»: Дан словарь grades={'Ivan':[4,5,4], 'Anna':[5,5,5],'Petr':[3,4,4]}.
#  Напишите цикл, который посчитает средний балл каждого ученика.
# Выведите имена тех, у кого средний балл >= 4.5.

# grades={'Ivan':[4,5,4], 'Anna':[5,5,5],'Petr':[3,4,4]}

# for name, scores in grades.items():
#     average = sum(scores)/len(scores)
#     if average >= 4.5:
#         print(name)

