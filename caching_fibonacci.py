def caching_fibonacci():
    # Створюємо словник для зберігання результатів обчислень
    cache = {}

    # Функція для обчислення числа Фібоначчі з використанням кешування
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        # Обчислюємо значення та зберігаємо його у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610