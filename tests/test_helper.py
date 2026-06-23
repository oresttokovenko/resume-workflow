from __future__ import annotations

from typing import TYPE_CHECKING

from tailor.helper import create_dir_and_files

if TYPE_CHECKING:
    from pathlib import Path


def test_creates_company_and_job_dir(workdir: Path) -> None:
    """A new company and job should create the expected directory structure."""
    create_dir_and_files("Meta", "Software Engineer")

    job_dir = workdir / "Meta" / "software_engineer"
    assert job_dir.is_dir()
    assert (job_dir / "job_description.txt").is_file()


def test_creates_second_job_in_existing_company(workdir: Path) -> None:
    """Adding a second job to an existing company directory works."""
    create_dir_and_files("Meta", "Software Engineer")
    create_dir_and_files("Meta", "Platform Engineer")

    assert (workdir / "Meta" / "software_engineer").is_dir()
    assert (workdir / "Meta" / "platform_engineer").is_dir()


def test_duplicate_job_name_is_rejected(workdir: Path) -> None:
    """Creating the same job twice should not overwrite or crash."""
    create_dir_and_files("Meta", "Staff Engineer")
    create_dir_and_files("Meta", "Staff Engineer")

    job_dir = workdir / "Meta" / "staff_engineer"
    assert job_dir.is_dir()
    assert (job_dir / "job_description.txt").is_file()


def test_no_template_is_honored(workdir: Path) -> None:
    """When use_template is False, template contents are not copied."""
    template = workdir / "_template"
    template.mkdir()
    (template / "resume.typ").touch()

    create_dir_and_files("Apple", "Data Engineer", use_template=False)

    job_dir = workdir / "Apple" / "data_engineer"
    assert not (job_dir / "resume.typ").exists()


def test_template_is_copied_when_enabled(workdir: Path) -> None:
    """When use_template is True (default) and a template dir exists, contents are copied."""
    template = workdir / "_template"
    template.mkdir()
    (template / "resume.typ").touch()
    fonts = template / "fonts"
    fonts.mkdir()
    (fonts / "main.otf").touch()

    create_dir_and_files("Apple", "Data Engineer", use_template=True)

    job_dir = workdir / "Apple" / "data_engineer"
    assert (job_dir / "resume.typ").is_file()
    assert (job_dir / "fonts" / "main.otf").is_file()
