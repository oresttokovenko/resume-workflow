from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture
def workdir(tmp_path: Path) -> Generator[Path]:
    """Change CWD to a temporary directory for the duration of the test.

    The directory (and all created files) is automatically removed by pytest
    after the test session.
    """
    cwd = Path.cwd()
    d = tmp_path / "workdir"
    d.mkdir()
    os.chdir(d)
    try:
        yield d
    finally:
        os.chdir(cwd)
