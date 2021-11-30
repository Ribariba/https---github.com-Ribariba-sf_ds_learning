"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number):
    count = 0 #счетчик попыток
    max_number = 101 #исходные границы
    min_number = 0
    while True:
        count += 1
        predict_number = (max_number + min_number) // 2 #
        if predict_number == number:
            return count
        elif predict_number > number: #перезаписываем границы диапозона, пока не отгадаем число
            max_number = predict_number
        elif predict_number < number:
            min_number = predict_number

final_count = random_predict(number)

print(f'Отгадали число {number} за {final_count} попыток!')

if __name__ == "__main__":
    # RUN
    random_predict(number)
