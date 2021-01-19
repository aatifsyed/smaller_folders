import logging as logger
from pathlib import Path

import pytest
from smaller_folders.cli import ArgumentParser


@pytest.fixture
def argument_parser() -> ArgumentParser:
    return ArgumentParser()


def test_parse_many_files(argument_parser: ArgumentParser):
    config = argument_parser.parse_args_to_config("a b c".split())
    assert config.files == [Path("a"), Path("b"), Path("c")]


def test_ignore_log_level_with_many_files(argument_parser: ArgumentParser):
    config = argument_parser.parse_args_to_config("-l info a b c".split())
    assert config.files == [Path("a"), Path("b"), Path("c")]