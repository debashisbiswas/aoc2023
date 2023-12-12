import os
import textwrap


def like_file(string: str) -> str:
    dedented = textwrap.dedent(string)
    return dedented.strip(os.linesep + " ")
