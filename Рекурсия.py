import graphics as gr


def factorial(n: int):
    assert n >= 0, "Error: n<0, not defined"
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(10))


# Алгоритм Евклида


def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


print(gcd(10, 10))


###


def matryoshka(n: int):
    if n == 1:
        print("Final n =", n)
    else:
        print("Current up n =", n)
        matryoshka(n - 1)
        print("Current down n =", n)


matryoshka(3)

window = gr.GraphWin("Russian game", 600, 600)
alpha = 0.9


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] + alpha * (B[0] - A[0]), A[1] + alpha * (B[1] - A[1]))
    B1 = (B[0] + alpha * (C[0] - B[0]), B[1] + alpha * (C[1] - B[1]))
    C1 = (C[0] + alpha * (D[0] - C[0]), C[1] + alpha * (D[1] - C[1]))
    D1 = (D[0] + alpha * (A[0] - D[0]), D[1] + alpha * (A[1] - D[1]))
    fractal_rectangle(A1, B1, C1, D1, deep=deep - 1)


fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), deep=20)


# Быстрое возведение в степень


def power(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:  # нечетные степени
        return power(a, n - 1) * a
    else:  # четные степени
        return power(a * a, n // 2)


# Ханойские башни...


# Генерация всех перестановок
def generate_numbers(N: int, M: int, prefix=None):
    '''Генерирует все числа (с лидирующими нулями)
    в N-ричной системе счисления(N <= 10)
    длины М
    '''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


#generate_numbers(3, 3)


def find_in(number: int, A):
    """Ищет number в А и возвращате True,
     если такой есть, False, если такого нет
     """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def generate_permutation(N: int, M: int = -1, prefix=None):
    ''' Генерация всех перестановок N чисел
    в М позициях с префиксом prefix
    '''
    M = N if M == -1 else M  # По умолчанию N чисел в М позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=',', sep="")
        return
    for number in range(1, N+1):
        if find_in(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()


generate_permutation(3)


# Рекуррентные сортировки
# 1) Быстрая сортировка Тони Хоара W(N*logN)

# 2) Сортировка слиянием W(N*logN)
# Слияние отсортированных массивов


def merge(A: list, B: list):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C

# Вторая реализация

input()
