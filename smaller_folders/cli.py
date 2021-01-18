import logging
import argparse
from pathlib import Path
import dataclasses
from typing import List

logger = logging.getLogger(__name__)


def main():
    logger.debug("Invoked at cli.py:main")

    config = ArgumentParser().parse_args_to_config()
    logger.debug(config)

    config.apply_to_logger(logger)


@dataclasses.dataclass
class ProgramConfig:
    log_level: str
    files: List[Path] = dataclasses.field(default_factory=list)

    def apply_to_logger(self, logger: logging.Logger):
        logger.setLevel(
            level=getattr(
                logging,
                self.log_level.upper(),
            )
        )
        logger.addHandler(logging.StreamHandler())


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument(
            "-l",
            "--log-level",
            choices=[
                "debug",
                "info",
                "warning",
                "error",
                "critical",
            ],
            default="info",
            help="set logging level for this tool",
            type=str,
        )
        self.add_argument("files", nargs="*", type=Path)

    def parse_args_to_config(self, *args, **kwargs) -> ProgramConfig:
        args = self.parse_args(*args, **kwargs)
        return ProgramConfig(log_level=args.log_level, files=args.files)
