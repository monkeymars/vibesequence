"""Atheris fuzz target: feed arbitrary bytes to the Python extractor as a source file.

Run: python fuzz/fuzz_python_extractor.py -max_total_time=60
"""
import sys
import tempfile
from pathlib import Path

import atheris

with atheris.instrument_imports():
    from vibesequence.extractors.python_ast import PythonAstExtractor

ROOT = Path(tempfile.mkdtemp())
SRC = ROOT / "pkg" / "mod.py"
SRC.parent.mkdir()
EXTRACTOR = PythonAstExtractor()


def test_one_input(data: bytes) -> None:
    SRC.write_bytes(data)
    try:
        EXTRACTOR.extract(SRC, ROOT)
    except (SyntaxError, ValueError, RecursionError, MemoryError):
        pass  # invalid or pathological source is rejected by ast.parse; anything else is a bug


if __name__ == "__main__":
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()
