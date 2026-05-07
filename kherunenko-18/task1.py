import os

# Назва змінної
var_name = "MY_SURNAME"
# Зчитуємо значення змінної
surname = os.getenv(var_name)

if surname:
    print(f"Значення системної змінної {var_name}: {surname}")
else:
    print(f"Помилка: Системна змінна {var_name} відсутня або не задана!")