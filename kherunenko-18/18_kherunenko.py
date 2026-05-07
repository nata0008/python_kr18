import sys

# ANSI-коди для кольорів 
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

#Заданий масив 
arr = [5, 3, -6, 5, 0, 3, 1, -4, 1, 3, 9, 0, 6, 1, 8, 4, 4, -1, 1, 12, 10, 9, 1, 7, 7, 11, 12, 16, 23, 9, 7, 3]

# Вивід заголовка (число 32 синім)
print(f"Масив {BLUE}32{RESET} елементів:")

# Вивід масиву: непарні - чорні (жирні) з *, парні - червоні без *
for num in arr:
    if num % 2 != 0:
        print(f"{BOLD}{num}*{RESET}", end=" ")
    else:
        print(f"{RED}{num}{RESET}", end=" ")
print("\n") 

# Ввід числа p
try:
    p_input = input(f"Введіть ціле число {BOLD}p{RESET}: ")
    p = int(p_input)
except ValueError:
    print("Потрібно ввести ціле число!")
    sys.exit(1)

# Підрахунок непарних елементів
count_less = sum(1 for x in arr if x % 2 != 0 and x < p)
count_greater_equal = sum(1 for x in arr if x % 2 != 0 and x >= p)

# Вивід результатів з кольорами
print(f"Кількість непарних елементів ( < {BLUE}{p}{RESET} ): {RED}{count_less}{RESET}")
print(f"                             (>= {BLUE}{p}{RESET}): {RED}{count_greater_equal}{RESET}")

# Порівняння
if count_less < count_greater_equal:
    print(f"Кількість непарних елементів (< {BLUE}{p}{RESET}) МЕНША!")
elif count_less > count_greater_equal:
    print(f"Кількість непарних елементів (< {BLUE}{p}{RESET}) БІЛЬША!")
else:
    print(f"Кількість непарних елементів (< {BLUE}{p}{RESET}) ОДНАКОВА!")