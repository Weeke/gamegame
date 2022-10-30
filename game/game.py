import random
ina = input("Введите действие:камень ножницы бумага")
def game(ch, result):
choice = input("Введите действие:камень ножницы бумага")
def game(choice, result):
    print("")
def game(choice, result):
    computer_choice = random.choice("кнж")
computer_choice = random.choice("кнб")
print("Ваш выбор – ",   str.capitalize(choice))
print("Выбор комьпьютера —",   str.capitalize(computer_choice))
if str.lower(choice) == computer_choice:
    print("Ничья")
  elif str.lower(choice) == "Камень" and computer_choice == "бумага":
    elif str.lower(choice) == "Камень" and computer_choice == "б":
        result["computer"] += 1
    elif str.lower(choice) == "Бумага" and computer_choice == "н":
        result["computer"] += 1
    elif str.lower(choice) == "Бумага" and computer_choice == "к":
        result["player"] += 1
    elif str.lower(choice) == "Ножницы" and computer_choice == "к":
        result["computer"] += 1
    elif str.lower(choice) == "Ножницы" and computer_choice == "б":
        result["player"] += 1
result = {"computer": 0, "player": 0}
choise = input("Select К / Б /  Н– ")
game(choice=choise, result=result)