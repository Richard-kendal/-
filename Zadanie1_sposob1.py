import random

def guess_number():
    number = random.randint(1, 100)
    low, high = 1, 100
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1
        print(f"Попытка {attempts}: пробуем {mid}")

        if mid < number:
            print("Больше")
            low = mid + 1
        elif mid > number:
            print("Меньше")
            high = mid - 1
        else:
            print(f"Угадали! Число {number} за {attempts} попыток.")
            break

guess_number()
