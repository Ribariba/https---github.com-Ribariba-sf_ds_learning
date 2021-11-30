"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number):   
    count = 0
    predict_number = 50 #сходу проверяем в каком отрезке искать (до 50 или после)
    count += 1
    if predict_number == number:
        print(f'Отгадали число {number} за {count} попыток!')      #на случай если загаданное число было 50
    elif predict_number > number:
        predict_number = 25
    elif predict_number < number:
        predict_number = 75
    while True:
        count += 1
        if count > 20:                                            #проверяем не проиграли ли мы еще)
            break
        elif number == predict_number:
            break
        elif number > predict_number:
            predict_number = predict_number + 2
            if number < predict_number:
                count += 1
                predict_number = predict_number - 1
        elif number < predict_number:
            predict_number = predict_number - 2
            if number > predict_number:
                count += 1
                predict_number = predict_number + 1   
    return count

count = random_predict(number)
                  
print(f'Отгадали число {number} за {count} попыток!')   

if __name__ == "__main__":
    # RUN
    random_predict(number)
