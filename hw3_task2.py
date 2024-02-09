TEXT = "Python is an interpreted, high-level, general-purpose programming language. \
    Created by Guido van Rossum and first released in 1991, Python's design philosophy \
    emphasizes code readability with its notable use of significant whitespace. Its \
    language constructs and object-oriented approach aim to help programmers write clear, \
    logical code for small and large-scale projects."

def freq_dict(text: str = TEXT, most_freq: int = 10, verbose: bool = False) -> dict:

    """
    В большой текстовой строке считает количество встречаемых слов
    и возвращает 10 самых частых. Не учитывает знаки препинания и регистр символов.
    Слова разделяются пробелами, апостроф не считается за пробел. Такие слова,
    как don t, it s, didn t итд (после того, как убрали знак препинания и апостроф), считаются двумя словами.
    Результат отсортирован по убыванию значения количества повторений слов.
    """

    fr_dict = {}
    text = text.lower()
    for char in "'.,-!?": # would be faster with re?
        text = text.replace(char, " ")
    text = text.split()
    text = [word for word in text if not word.isdigit()]
    for word in text:
        fr_dict[word] = fr_dict.get(word, 0) + 1
    fr_list = [(word, freq) for word, freq in fr_dict.items()]
    fr_list.sort(reverse=True, key=lambda arg: arg[1])
    return fr_list if verbose else fr_list[:most_freq]

if __name__ == "__main__":
    print(freq_dict(2**0.5, b'Vote for Nadejdin!!!', "Pet Hein", True))