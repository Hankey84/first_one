# Извините что не на псевдокоде, мне так проще ;)
numbers = [2, 5, 13, 7, 6, 4]
size = len(numbers)
summ = 0  # чтобы не путать со втроенной функцией sum()
avg = 0
index = 0

while index < size:
    summ += numbers[index]
    index += 1
avg = round(summ / size)  # Тоже не люблю вещественные числа

print (f'Среднее арифметическое массива = %d'%(avg))

