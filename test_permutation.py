from itertools import permutations

# --- Словарь соответствия букв и позиций ---
letters_numbers_pairs = {
    'K': ['1', '3', '5', '6', '8'],  # K соответствует этим цифрам
    'I': ['2'],  # I = 2
    'D': ['4'],  # D = 4
    'H': ['7']   # H = 7
}

# Пары позиций, которые фиксируются в начале
required_pairs = [(8, 5), (5, 8)]
remaining_positions = [1, 2, 3, 4, 6, 7]

def generate_permutations():
    """Генерация всех перестановок с учётом первых пар."""
    all_permutations = []
    for pair in required_pairs:
        for perm in permutations(remaining_positions):
            all_permutations.append(tuple(pair) + perm)
    return all_permutations

def find_letter_by_position(position, permutation):
    """Находит букву, соответствующую позиции в permutation."""
    for letter, positions in letters_numbers_pairs.items():
        if str(position) in positions:
            return letter
    return '?'  # Если позиция не найдена

def create_encoding_dict(permutation, word):
    """Создаёт словарь кодировки на основе permutation и слова."""
    encoding_dict = {}
    pairs = [word[i:i+2] for i in range(0, len(word), 2)]  # Разбиваем слово на пары
    for i, pair in enumerate(pairs):
        pos1 = permutation[i * 2]
        pos2 = permutation[i * 2 + 1]
        letter1 = find_letter_by_position(pos1, permutation)
        letter2 = find_letter_by_position(pos2, permutation)
        key = f"{letter1}{letter2}"
        encoding_dict[key] = pair

    # Добавляем правило для буквы 'а'
    a_cipher = "AN" if permutation[:2] == (8, 5) else "NA"
    encoding_dict[a_cipher] = 'а'
    return encoding_dict

def generate_all_encoding_dicts(word):
    """Генерация всех возможных словарей кодировки для заданного слова."""
    all_dicts = []
    permutations_list = generate_permutations()
    for perm in permutations_list:
        encoding_dict = create_encoding_dict(perm, word)
        all_dicts.append((perm, encoding_dict))
    return all_dicts

# Слово для кодировки
word = "бомба"

# Генерация словарей
all_encoding_dicts = generate_all_encoding_dicts(word)

# Вывод результатов в нужном формате
for i, (perm, d) in enumerate(all_encoding_dicts[:16], 1):  # Вывод первых 16 результатов
    print(f"Permutation {i}: {perm}")
    print(f"Encoding_dict: {d}\n")
