# Задание 1
def first_task():
    my_list = [1, 7, 3, 9, 4, 5, 0, 10, 25, 15, 30]
    # 1. Создайте новый список из элементов my_list, которые меньше 5.
    first_list = [x for x in my_list if x < 5]
    print(first_list)

    # 2. Создайте новый список из элементов my_list, деленных на 2.
    second_list = [x / 2 for x in my_list]
    print(second_list)

    # 3. Создайте новый список из элементов my_list, которые больше 17, умножив их на 2.
    third_list = [x * 2 for x in my_list if x > 17]
    print(third_list)

    # 4. Создайте список, включающий числа от 0 до введённого пользователем, возведённые в квадрат.
    fourth_list = [x ** 2 for x in range(int(input("Введите число: ")) + 1)]
    print(fourth_list)

    # 5. Используя списочное выражение и метод split, составьте список из введённых чисел, записанных на одной
    #    строке без указания заранее их количества; затем выведите их квадраты также на одной строке.
    fifth_list = [str(int(x) ** 2) for x in input("Введите числа: ").split()]
    print(" ".join(fifth_list))

    # 6. Используя списочное выражение и метод split, составьте список из введённых чисел, записанных на одной
    #    строке без указания заранее их количества; затем выведите на одной строке только те квадраты нечетных
    #    чисел, которые не заканчиваются на цифру 9. Постарайтесь решить данную задачу в одну строку.
    print(" ".join([str(int(x) ** 2) for x in input("Введите числа: ").split() if int(x) % 2 != 0 and (int(x) ** 2) % 10 != 9]))


# Задание 2
def second_task():
    result = ["*" * int(x) for x in input().split()]
    print("\n".join(result))


# Задание 3
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")


# Задание 4
def distance(x1, y1, x2, y2):
    return pow((x2 - x1) ** 2 + (y2 - y1) ** 2, 0.5)


# Задание 5
def number_to_words(n):
    units = [
        "", "один", "два", "три", "четыре", "пять",
        "шесть", "семь", "восемь", "девять"
    ]
    two_digit = [
        "десять", "одиннадцать", "двенадцать", "тринадцать",
        "четырнадцать", "пятнадцать", "шестнадцать",
        "семнадцать", "восемнадцать", "девятнадцать"
    ]
    tens = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят",
        "шестьдесят", "семьдесят", "восемьдесят", "девяносто"
    ]

    if 1 <= n <= 9:
        return units[n]

    elif 10 <= n <= 19:
        return two_digit[n - 10]

    elif 20 <= n <= 99:
        ten = n // 10
        unit = n % 10

        if unit == 0:
            return tens[ten]
        else:
            return tens[ten] + " " + units[unit]


# Задание 6
def bracket_check(test_string):
    counter = 0

    for char in test_string:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

        if counter < 0:
            return "NO"

    if counter == 0:
        return "YES"
    else:
        return "NO"


# Задание 7
def palindrome(s):
    entered_string = s.lower().replace(" ", "")

    if entered_string == entered_string[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"


# Задание 8
def tic_tac_toe(field):
    lines = [
        field[0], field[1], field[2],

        [field[0][0], field[1][0], field[2][0]],
        [field[0][1], field[1][1], field[2][1]],
        [field[0][2], field[1][2], field[2][2]],

        [field[0][0], field[1][1], field[2][2]],
        [field[0][2], field[1][1], field[2][0]]
    ]

    for line in lines:
        if len(set(line)) == 1 and line[0] != "-":
            print(f"{line[0]} win")
            return

    print("draw")


# Задание 9
last_message = None


def print_without_duplicates(message):
    global last_message

    if message != last_message:
        print(message)
        last_message = message


# Задание 10
alice_friends = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person not in alice_friends:
        alice_friends[name_of_person] = set()

    alice_friends[name_of_person].update(list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    person1_friends = alice_friends.get(name_of_person1, set())

    return name_of_person2 in person1_friends


def print_friends(name_of_person):
    person_friends = alice_friends.get(name_of_person, set())

    person_friends = sorted(person_friends)

    print(" ".join(person_friends))


# Задание 11
one = 17
two = 89
three = None


def roman():
    global three
    three = one + two
    roman_str = []

    roman_numbers = [
        (1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"),
        (40, "XL"), (50, "L"), (90, "XC"), (100, "C"),
        (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")
    ]

    for number in (one, two, three):
        roman_string = ""
        for value, symbol in reversed(roman_numbers):
            while number >= value:
                roman_string += symbol
                number -= value

        roman_str.append(roman_string)

    print(f"{roman_str[0]} + {roman_str[1]} = {roman_str[2]}")


# Задание 12
def twelfth_task():
    # Неизменяемые типы

    # Оператор +
    num1 = 10
    print(f"До +: num1 = {num1}, id(num1) = {id(num1)}")
    num1 = num1 + 5  # Создается новый объект
    # ID объекта изменился
    print(f"После +: num1 = {num1}, id(num1) = {id(num1)}")

    # Оператор +=
    num2 = 10
    print(f"До +=: num2 = {num2}, id(num2) = {id(num2)}")
    num2 += 5  # Создается новый объект.
    # ID объекта изменился
    print(f"После +=: num2 = {num2}, id(num2) = {id(num2)}")

    # Изменяемые типы

    # Оператор +
    list1 = [1, 2, 3]
    print(f"До +: list1 = {list1}, id(list1) = {id(list1)}")
    list1 = list1 + [4, 5]  # Создается новый список.
    # ID списка изменился
    print(f"После +: list1 = {list1}, id(list1) = {id(list1)}")

    # Оператор +=
    list2 = [1, 2, 3]
    ref_list2 = list2  # ref_list2 указывает на тот же участок памяти, что и list2
    print(f"До +=: list2 = {list2}, id(list2) = {id(list2)}")
    # Операция += для списков модифицирует текущий список. Новый объект не создается.
    list2 += [4, 5]
    # ID списка остался прежним
    print(f"После +=: list2 = {list2}, id(list2) = {id(list2)}")
    # Так как сам объект в памяти изменился, все ссылки на него тоже покажут новые данные (изменятся)
    print(f"Вторая ссылка: ref_list2 = {ref_list2}")


# Задание 13
def thirteen_task():
    # Использование метода sorted()

    list_a = [5, 2, 8, 1, 3]  # Создание некоторого списка a
    print(f"Исходный список list_a: {list_a}")
    print(f"ID исходного списка list_a до сортировки: {id(list_a)}")
    # Применяем sorted() и присваиваем результат переменной list_b
    list_b = sorted(list_a)
    print(f"Новый список list_b: {list_b}")
    print(f"Исходный список list_a: {list_a}")
    print(f"ID нового списка list_b: {id(list_b)}")
    print(f"ID исходного списка list_a после функции: {id(list_a)}")
    # Старый список list_a остался нетронутым, его ID остался прежним.
    # Метод sorted() создал новый список list_b, содержащий отсортированные элементы list_a.

    # Использование метода sort()
    list_a = [5, 2, 8, 1, 3]  # Повторное создание некоторого списка a
    print(f"Исходный список list_a: {list_a}")
    print(f"ID исходного списка list_a до сортировки: {id(list_a)}")
    # Применяем метод sort() и присваиваем результат переменной list_b
    list_b = list_a.sort()
    print(f"Переменная list_b: {list_b}")
    print(f"Исходный список list_a: {list_a}")
    print(f"ID новой переменной list_b: {id(list_b)}")
    print(f"ID исходного списка list_a после функции: {id(list_a)}")
    # Старый список list_a был отсортирован, но его ID остался прежним.
    # Метод sort() вернул значение None, которое было присвоено переменной list_b вместо отсортированного
    # списка.


# Задание 14
def fourteen_task():
    # Код выполняет разделение исходного списка чисел на два списка: чётных и нечётных чисел.
    # Поскольку во второй строке odd = even = [] переменные odd и even записаны через равенство,
    # они обе указывают на один участок в памяти, что, по сути, означает создание лишь одного списка
    # и двух ссылок, указывающих на него. В результате этого, как список odd, так и список even
    # (являющиеся одним и тем же списком) содержат все элементы исходного списка numbers.
    # Для правильной реализации логики кода, необходимо объявлять оба списка независимо.
    numbers = [2, 5, 7, 7, 8, 4, 1, 6]
    odd = []  # Отдельное объявление списка odd
    even = []  # Отдельное объявление списка even

    for number in numbers:  # Перебор всех элементов списка numbers
        if number % 2 == 0:  # Проверка каждого элемента на соответствие условию чётности
            even.append(number)  # Добавление в список even
        else:
            odd.append(number)  # Добавление в список odd


# Задание 15
fractal = [0, None, None, 2]

fractal[1] = fractal
fractal[2] = fractal
# Второй и третий элементы списка являются ссылками на этот же список, создавая фрактал.


# Задание 16
# В строке исходной функции sequence = sequence + [next_element] создается новая локальная переменная
# sequence, которая исчезает после выполнения функции. Для модификации списка (изменяемого типа данных)
# можно использовать метод append(), который добавляет новый элемент в конец списка, модифицируя его, и не
# создавая нового объекта.
def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)  # Добавление нового элемента в исходный список


# Задание 17
def mirror(arr):
    mirrored_part = reversed(arr)
    arr += mirrored_part


# Задание 18
def from_string_to_list(string, container):
    container.extend(int(x) for x in string.split())


# Задание 19
def transpose(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    new_matrix = []

    for col in range(n_cols):
        new_row = []

        for row in range(n_rows):
            new_row.append(matrix[row][col])

        new_matrix.append(new_row)

    matrix[:] = new_matrix


# Задание 20
def swap(first, second):
    first[:], second[:] = second[:], first[:]


# Задание 21
def defractalize(fracta1):
    for i in range(len(fracta1) - 1, -1, -1):
        if fracta1[i] is fracta1:
            del fracta1[i]


# Задание 22
def fractal_print(obj):
    def format_item(item, depth):
        if item is obj:

            if depth == 2:
                return "[...]"

            elements = [format_item(x, depth + 1) for x in item]
            return "[" + ", ".join(elements) + "]"

        else:
            return repr(item)

    print(format_item(obj, 0))


# Задание 23
def matrix(n=1, m=None, a=0):

    if m is None:
        m = n

    return [[a for _ in range(m)] for _ in range(n)]


# Задание 24
def partial_sums(*args):
    result = [0]

    current_sum = 0

    for num in args:
        current_sum += num
        result.append(current_sum)

    return result


# Задание 25
def solve(*coefficients):
    n = len(coefficients)
    if n == 0 or n > 3:
        return None

    # Распределяем коэффициенты a, b, c в зависимости от их количества
    if n == 3:
        a, b, c = coefficients
    elif n == 2:
        a = 0
        b, c = coefficients
    elif n == 1:
        a = 0
        b = 0
        c = coefficients[0]

    # Квадратное уравнение
    if a != 0:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return []
        elif D == 0:
            return [-b / (2 * a)]
        else:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            return [x1, x2]

    # Линейное уравнение
    elif b != 0:
        return [-c / b]

    # Константа c
    else:
        if c == 0:
            return ["all"]
        else:
            return []


def main():
    # Задание 1
    first_task()

    # Задание 2
    second_task()

    # Задание 3
    triangle(1, 1, 2)
    triangle(7, 6, 10)

    # Задание 4
    print(distance(0, 0, 3, 4))

    # Задание 5
    print(number_to_words(4))
    print(number_to_words(13))

    # Задание 6
    print(bracket_check("()"))
    print(bracket_check("((()(()"))

    # Задание 7
    print(palindrome("А роза упала на лапу Азора"))
    print(palindrome("Палиндром"))

    # Задание 8
    field = [
        ["0", "-", "0"],
        ["x", "x", "x"],
        ["0", "0", "-"]
    ]
    tic_tac_toe(field)

    # Задание 9
    print_without_duplicates("Привет")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Когда доедешь до дома")
    print_without_duplicates("Ага, жду")
    print_without_duplicates("Ага, жду")

    # Задание 10
    add_friends("Алла", ["Марина", "Иван"])
    print(are_friends("Алла", "Мария"))
    add_friends("Алла", ["Мария"])
    print(are_friends("Алла", "Мария"))

    # Задание 11
    roman()

    # Задание 12
    twelfth_task()

    # Задание 13
    thirteen_task()

    # Задание 14
    fourteen_task()

    # Задание 16
    sequence = [1, 1]
    continue_fibonacci_sequence(sequence, 1)
    print(*sequence)

    # Задание 17
    arr = [1, 2]
    mirror(arr)
    print(*arr)

    # Задание 18
    a = [1, 2, 3]
    from_string_to_list("1 3 99 52", a)
    print(*a)

    # Задание 19
    matrix_19 = [[1]]
    transpose(matrix_19)
    for line in matrix_19:
        print(*line)

    # Задание 20
    first = [1, 2, 3]
    second = [4, 5, 6]
    first_content = first[:]
    second_content = second[:]
    swap(first, second)
    print(first, second_content, first == second_content)
    print(second, first_content, second == first_content)

    # Задание 21
    fractal_21 = [2, 5]
    fractal_21.append(fractal_21)
    fractal_21.append(3)
    defractalize(fractal_21)
    print(fractal_21)

    # Задание 22
    fractal_22 = [3]
    fractal_22.append(fractal_22)
    fractal_print(fractal_22)

    # Задание 23
    rows = matrix()
    for row in rows:
        print(*row)

    rows2 = matrix(2)
    for row in rows2:
        print(*row)

    # Задание 24
    print(partial_sums(1, 0.5, 0.25, 0.125))

    # Задание 25
    print(sorted(solve(1, 2, 1)))
    print(sorted(solve(1, -3, 2)))


main()
