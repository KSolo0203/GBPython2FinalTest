import argparse

def parse_args(args):
    hw15_argparser = argparse.ArgumentParser(description="Argparser for last homework")

    hw15_argparser.add_argument(
        "-path", metavar="PATH",
        type=str,
        help="Path to file from the frequency dictionary is required to be created.\n \
            Default test text used if argument is omitted"
    )

    hw15_argparser.add_argument(
        "-most_freq", metavar="MFRQ",
        type=int,
        help="Size of dictionary that contains most frequntly entries in the text.\n \
            Default 10 size set if argument is omitted"
    )

    hw15_argparser.add_argument(
        "-verbose",
        action="store_true",
        help="If argument set to True the size of dictionary is unlimited"
    )

    return hw15_argparser.parse_args(args)