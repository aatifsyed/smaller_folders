import logging
import argparse

logger = logging.getLogger(__name__)


def main():
    logger.debug("Invoked at cli.py:main")

    args = parse_arguments()
    configure_logger(logger, args)

    logger.debug(args)


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="smaller_folders",
        # NOTE this must be kept in sync with `pyproject.toml`
        description="Split an arbitrary number of files into sub-folders containing a specified number of files each.",
    )
    parser.add_argument(
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
    args = parser.parse_args()
    return args


def configure_logger(logger: logging.Logger, args: argparse.Namespace):
    logger.setLevel(
        level=getattr(
            logging,
            args.log_level.upper(),
        )
    )
    logger.addHandler(logging.StreamHandler())