import pytest
from argparse import Namespace
from main import main
import logging
from hw3_task2 import freq_dict, TEXT
from hw15_file_reading import text_loader
from hw15_logger import hw15_logger
from hw15_argparser import parse_args


def test_freq_dict_args():
    assert freq_dict(TEXT, 10, False) == [
        ('and', 3), ('python', 2), ('language', 2),
        ('code', 2), ('its', 2), ('is', 1), ('an', 1),
        ('interpreted', 1), ('high', 1), ('level', 1)
    ]

def test_freq_dict_noargs():
    assert freq_dict() == [
        ('and', 3), ('python', 2), ('language', 2),
        ('code', 2), ('its', 2), ('is', 1), ('an', 1),
        ('interpreted', 1), ('high', 1), ('level', 1)
    ]

def test_freq_dict_incorrect_args():
    with pytest.raises(TypeError):
        freq_dict(2**0.5, b'Vote for Nadejdin!!!', "Pet Hein", True)

def test_arg_parser():
    assert parse_args(["-most_freq", "2"]) == Namespace(path=None, most_freq=2, verbose=False)

def test_logger(caplog):
    with caplog.at_level(logging.WARNING):
         main()
    assert "" in caplog.text