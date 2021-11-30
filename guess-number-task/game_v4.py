"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number):
    count = 0 #счетчик попыток
    max_number = 101 #исходные границы
    min_number = 0
    while True:
        count += 1
        predict_number = (max_number + min_number) // 2 
        if predict_number == number:
            return count
        elif predict_number > number: #перезаписываем границы диапозона, пока не отгадаем число
            max_number = predict_number
        elif predict_number < number:
            min_number = predict_number

final_count = random_predict(number)

print(f'Отгадали число {number} за {final_count} попыток!')

def score_game(random_predict):
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)

