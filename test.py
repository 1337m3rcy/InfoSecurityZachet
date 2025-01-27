from itertools import permutations

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
                return False

    # Проверяем совпадение первой и последней пары
    return same_letter_pair(perm)

# --- Генерация всех возможных перестановок ---
def generate_all_permutations():
    digits = [1, 2, 3, 4, 5, 6, 7, 8]
    all_perms = list(permutations(digits))
    valid_perms = []

    for perm in all_perms:
        if check_permutation(perm):
            valid_perms.append(perm)

    return valid_perms

# --- Запись валидных перестановок в файл ---
def write_valid_permutations_to_file(valid_perms, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for perm in valid_perms:
            f.write(f"Permutation: {perm}\n")
            # Здесь можно добавить дополнительные данные, если нужно
            f.write("\n")

# --- Основная функция ---
def main():
    valid_perms = generate_all_permutations()
    print(f"Найдено {len(valid_perms)} валидных перестановок.")
    write_valid_permutations_to_file(valid_perms, "valid_results.txt")

# --- Запуск программы ---
if __name__ == "__main__":
    main()