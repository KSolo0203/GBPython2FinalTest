from pathlib import Path

def text_loader(path: str | Path) -> str:

    """
    Читает файл по указанному адресу, возвращает содержимое в строковом представлении.
    Обработка ошибок осуществляется в вызывающей функции. 
    """

    with open(path, "r", encoding="utf-8") as source:
            text = source.read()
    return text