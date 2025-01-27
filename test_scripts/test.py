# def extract_permutations(filename, output_file):
#     with open(filename, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#
#     results = []
#     capture = False
#     temp_result = ""
#
#     for line in lines:
#         if line.startswith("Permutation:"):
#             # Проверяем, содержит ли строка [5, 8 или [8, 5
#             if "Permutation: [5, 8" in line or "Permutation: [8, 5" in line:
#                 capture = True
#                 temp_result = line  # Начинаем новую запись
#             else:
#                 capture = False
#
#         if capture:
#             temp_result += line
#             # Если достигли конца блока, добавляем в результаты
#             if line == "\n":
#                 results.append(temp_result)
#                 capture = False
#
#     # Сохранение результатов в новый файл
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write("".join(results))
#
#     print(f"Готово! Найдено {len(results)} подходящих перестановок.")
#     print(f"Результаты сохранены в {output_file}")
#
#
# # Запуск скрипта
# extract_permutations("results.txt", "filtered_results.txt")


def extract_bomba_permutations(filename, output_file):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    results = []
    capture = False
    temp_result = ""

    for line in lines:
        if line.startswith("Permutation:"):
            # Проверяем, начинается ли перестановка с [5, 8] или [8, 5]
            if "Permutation: [5, 8" in line or "Permutation: [8, 5" in line:
                capture = True
                temp_result = line  # Сохраняем перестановку
            else:
                capture = False

        if capture:
            temp_result += line
            # Ищем "б??ба" в расшифрованном тексте
            if "б??ба" in line:
                results.append(temp_result)
                capture = False
            if line == "\n":
                capture = False

    # Сохранение результатов в новый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("".join(results))

    print(f"Готово! Найдено {len(results)} совпадений с перестановками [5, 8] и [8, 5].")
    print(f"Результаты сохранены в {output_file}")


# Запуск фильтрации
extract_bomba_permutations("results.txt", "bomba_results.txt")


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

'''
нет, ты не понял, нужно составить именно словарь где ключ : значение будет цифра : буква и заттем отталкиваться от этого так 
как символы MB или BM это зашифрованные символы 

словарь будет таким number_pairs = {
    '1': "M",
    '2': "B",
    '3': "B",
    '4': "M",
    '5': "M",
    '6': "M",
    '7': "B",
    '8': "B",
}

т.е для Permutation [5, 8 (MB) для цифры 4 (M) например парой будет цифры 2, 3, 7 (B) так как они образуют пару MB, 
и будут пары такие 4,7 или 4,3 или 4,2 

а для Permutation [8, 5 (BM) для цифры 4 (M) цифры 2, 3, 7 будут образовывать пару в виде 2,4 или 3,4 или 7,4 т.е BM

Это всё нужно сделать для шага где мы искали перестановки 8! только первым шагом мы сужаем поиск до 5,8 или 8,5 а вторым шагом, мы следим за тем, чтобы пары 
соотвествовали друг друг т.е для 5,8 числа должны образовывать пару MB, а для 8,5 пару BM
'''