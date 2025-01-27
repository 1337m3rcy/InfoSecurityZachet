# # --- Словарь соответствий цифр символам (M или B) ---
# number_pairs = {
#     '1': "M",
#     '2': "B",
#     '3': "B",
#     '4': "M",
#     '5': "M",
#     '6': "M",
#     '7': "B",
#     '8': "B",
# }
#
#
# # --- Функция проверки пары чисел на соответствие MB/BM ---
# def is_valid_pair(a, b, mode):
#     return (number_pairs[str(a)], number_pairs[str(b)]) == ("M", "B") if mode == "MB" else \
#            (number_pairs[str(a)], number_pairs[str(b)]) == ("B", "M")
#
#
# # --- Функция проверки всей перестановки (по парам) ---
# def check_permutation(perm):
#     if perm[0] == 5 and perm[1] == 8:
#         mode = "MB"
#     elif perm[0] == 8 and perm[1] == 5:
#         mode = "BM"
#     else:
#         return False  # Если не 5,8 или 8,5 – отбрасываем
#
#     # Проверяем пары (0,1), (2,3), (4,5), (6,7)
#     for i in range(0, len(perm), 2):
#         if i + 1 < len(perm):
#             if not is_valid_pair(perm[i], perm[i + 1], mode):
#                 print(f"Отбрасываем {perm} – пара ({perm[i]}, {perm[i + 1]}) не прошла проверку [{mode}].")
#                 return False
#
#     print(f"Подходит: {perm} [{mode}].")
#     return True
#
#
# # --- Чтение и проверка results.txt ---
# def filter_results(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#
#     valid_results = []
#     current_permutation = None
#     temp_result = ""
#
#     for line in lines:
#         if line.startswith("Permutation:"):
#             # Сохраняем текущую перестановку и начинаем сбор данных
#             temp_result = line
#             current_permutation = list(map(int, line.strip().split("[")[1].split("]")[0].split(", ")))
#
#         elif line.strip():  # Добавляем текст результата к текущей перестановке
#             temp_result += line
#
#         if line == "\n" and current_permutation:
#             # Проверяем перестановку после блока
#             if check_permutation(current_permutation):
#                 valid_results.append(temp_result)
#             current_permutation = None
#
#     # Запись отфильтрованных результатов
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write("".join(valid_results))
#
#     print(f"Готово! Найдено {len(valid_results)} подходящих перестановок.")
#     print(f"Результаты сохранены в {output_file}")
#
#
# # --- Запуск фильтрации ---
# filter_results("results.txt", "valid_results.txt")
#

# --- Словарь цифр (M/B) ---
number_pairs = {
    '1': "M",
    '2': "B",
    '3': "B",
    '4': "M",
    '5': "M",
    '6': "M",
    '7': "B",
    '8': "B",
}

# --- Словарь букв (соответствие цифрам) ---
letters_numbers_pairs = {
    'K': ['1', '3', '5', '6', '8'],  # K соответствует этим цифрам
    'I': ['2'],  # I = 2
    'D': ['4'],  # D = 4
    'H': ['7']  # H = 7
}


# --- Функция проверки пары чисел на MB/BM ---
def is_valid_pair(a, b, mode):
    return (number_pairs[str(a)], number_pairs[str(b)]) == ("M", "B") if mode == "MB" else \
        (number_pairs[str(a)], number_pairs[str(b)]) == ("B", "M")


# --- Функция проверки первой и последней пары на одинаковую букву ---
def same_letter_pair(perm):
    first_pair = perm[0], perm[1]
    last_pair = perm[6], perm[7]

    # Первая и последняя пары
    first_set = {str(first_pair[0]), str(first_pair[1])}
    last_set = {str(last_pair[0]), str(last_pair[1])}

    for letter, nums in letters_numbers_pairs.items():
        # Если обе пары содержат одинаковые цифры из одного набора – ок
        if first_set.issubset(nums) and last_set.issubset(nums):
            return True

    # Если пары не соответствуют одному и тому же символу
    print(f"Отбрасываем {perm} – первая пара {first_pair} != последняя пара {last_pair}.")
    return False


# --- Функция проверки перестановки (по MB/BM и совпадению пар) ---
def check_permutation(perm):
    # Проверяем по правилу MB/BM
    if perm[0] == 5 and perm[1] == 8:
        mode = "MB"
    elif perm[0] == 8 and perm[1] == 5:
        mode = "BM"
    else:
        return False  # Если не 5,8 или 8,5 – отбрасываем

    # Проверяем все пары (0,1), (2,3), (4,5), (6,7)
    for i in range(0, len(perm), 2):
        if i + 1 < len(perm):
            if not is_valid_pair(perm[i], perm[i + 1], mode):
                print(f"Отбрасываем {perm} – пара ({perm[i]}, {perm[i + 1]}) не прошла проверку [{mode}].")
                return False

    # Проверяем совпадение первой и последней пары
    return same_letter_pair(perm)


# --- Чтение и проверка results.txt ---
def filter_results(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    valid_results = []
    current_permutation = None
    temp_result = ""

    for line in lines:
        if line.startswith("Permutation:"):
            # Сохраняем текущую перестановку и начинаем сбор данных
            temp_result = line
            current_permutation = list(map(int, line.strip().split("[")[1].split("]")[0].split(", ")))

        elif line.strip():  # Добавляем текст результата к текущей перестановке
            temp_result += line

        if line == "\n" and current_permutation:
            # Проверяем перестановку после блока
            if check_permutation(current_permutation):
                valid_results.append(temp_result)
            current_permutation = None

    # Запись отфильтрованных результатов
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("".join(valid_results))

    print(f"Готово! Найдено {len(valid_results)} подходящих перестановок.")
    print(f"Результаты сохранены в {output_file}")


# --- Запуск фильтрации ---
filter_results("results.txt", "valid_results_1.txt")


