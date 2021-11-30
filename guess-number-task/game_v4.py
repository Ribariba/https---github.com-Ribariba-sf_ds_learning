"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0 #счетчик попыток

max_number = 101  #исходные границы
min_number = 0

#перезаписываем границы диапозона, пока не отгадаем число

while True:
    count += 1
    predict_number = (max_number + min_number) // 2 
    if predict_number == number:
        print(f'Отгадали число {number} за {count} попыток!') 
        break
    elif predict_number > number:
        max_number = predict_number
    elif predict_number < number:
        min_number = predict_number
    
