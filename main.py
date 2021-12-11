# Лаораторная работа 9
# Отсортировать слова по возрастанию их длины и вернуть строку с предложением, в котором слова отсортированы
def sort_sentence(sentence):
    new_list = ""

    sentence = sentence.lower()
    stroke = sentence.split(" ")

    stroke.sort(key=len)
    stroke[0] = stroke[0].capitalize()

    for u in range(0, len(stroke)):
        new_list += stroke[u] + " "

    return new_list
