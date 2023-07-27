import os
from pathlib import Path

MNI_DATAPATH = Path(os.getenv('MNI_DATAPATH', None))
FILE_RESOLUTION_DESCRIPTION = 'Should be any of an absolute path, a relative path, ' \
                            'a path relative to the input directory, or a relative path to ' \
                            f'MNI_DATAPATH(={MNI_DATAPATH}).'
"""
An English description of how this program will resolve paths to data files.
"""


def find_template(p: str | os.PathLike, input_dir: Path) -> Path:
    """
    A function which implements the functionality described by the value of ``FILE_RESOLUTION_DESCRIPTION``.
    """
    to_check = (Path(p), input_dir / p, MNI_DATAPATH / p)
    for resolved_path in to_check:
        if resolved_path.is_file():
            return resolved_path
    raise FileNotFoundError(f"None of the following paths are a file: {to_check}")
