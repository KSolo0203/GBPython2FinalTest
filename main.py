
from hw3_task2 import freq_dict
from hw15_file_reading import text_loader
from hw15_logger import hw15_logger
from hw15_argparser import parse_args
import sys


def main():
    args = parse_args(sys.argv[1:]) # shit-taping for pytest
    if not args.path:
        result = freq_dict(most_freq=args.most_freq, verbose=args.verbose)
        hw15_logger.info(
            f"Модуль {__name__}, функция freq_dict()\n\
            Аргументы CLI: не переданы\n\
            Прочитан текст: по умолчанию.\n\
            Результаты:\n\
            {result}"
        )
    else:
        try:
            text = text_loader(args.path)
            result = freq_dict(text, most_freq=args.most_freq, verbose=args.verbose)
            hw15_logger.info(
                f"Модуль {__name__}, функция freq_dict()\n"
                f"Аргументы CLI: {args}\n"
                f"Прочитан текст: {args.path}\n"
                "Результаты:\n"
                f"{result}"
            )
        except FileNotFoundError as e:
            hw15_logger.error(
                f"Модуль {__name__}, функция freq_dict()\n"
                f"Аргументы CLI: {args}\n"
                f"Ошибка {e}"
            )

            
if __name__ == "__main__":
    main()
