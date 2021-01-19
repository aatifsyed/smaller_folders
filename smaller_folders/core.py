import logging
import math
import shutil

from more_itertools import chunked

from .program_config import ProgramConfig

logger = logging.getLogger(__name__)


def main(program_config: ProgramConfig):
    assert (
        program_config.destination_directory.is_dir()
    ), f"Supplied destination {program_config.destination_directory.absolute()} does not exist or is not a directory"

    for chunk_number, chunk in enumerate(
        chunked(program_config.files, program_config.number_per_folder), start=1
    ):
        logger.debug(f"chunk {chunk_number}, containing {len(chunk)} items")

        sub_folder_postfix = pad_sub_folder_number(chunk_number, program_config)

        sub_folder = program_config.destination_directory.joinpath(
            f"{program_config.sub_folder_prefix}{sub_folder_postfix}"
        )

        logger.debug(f"creating sub-folder {sub_folder.absolute()}")

        if sub_folder.is_dir():
            logger.info(
                f"A sub-folder, {sub_folder.absolute()}, already exists. Continuing."
            )
        else:
            sub_folder.mkdir()

        for file in chunk:
            if not file.is_file():
                logger.info(
                    f"A supplied path, {file.absolute()}, does not exist or is not a file. Skipping."
                )
                continue
            shutil.move(file, sub_folder)


def pad_sub_folder_number(number: int, program_config: ProgramConfig) -> str:
    max_number = len(program_config.files) + 1
    max_width = math.floor(math.log10(max_number)) + 1
    return str(number).rjust(max_width, "0")
