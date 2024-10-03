def task_1(a: int, b: int):

    if a > b:
        print(a)
    else:
        print(b)

print(task_1(100,60))

def task_2(a: int, b: int):
    if a - b >= 135 or b - a >= 135:
        print ("Yes")
    else:
        print("No")

print(task_2(200,400))

def task_3(a: int):

    if a == 1 or a == 2 or a == 12:
        print ("Зима")
    elif a == 3 or a == 4 or a == 5:
        print ("Весна")
    elif a == 6 or a == 7 or a == 8:
        print ("Лето")
    elif a == 9 or a == 10 or a == 11:
        print ("Осень")

print(task_3(5))

def task_4(a: int, b: int, c:int):
    if a > 10 and b > 10 and c > 10:
        print("Yes")
    else:
        print("No")


print(task_4(11,12,32))

def task_5(a: int, b: int):
    a = a * 365 + b * 29
    print (a)
print(task_5(3,6))


