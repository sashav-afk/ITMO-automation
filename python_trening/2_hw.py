def task_1(q: int, b: float, c: str, d:list, e: bool):
    return type(q), type(b), type(c), type(d), type(e)

print(task_1(10,10.0001, '10', [3,4,5,6], 10>9))

def task_2(a:list):
    return a[0:3]
print(task_2([1,2,3,5,8,13,21]))
#последовательность Фибоначчи

def task_3(m:int):
    return m*m
print(task_3(5))
