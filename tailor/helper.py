"""Filesystem operations for resume directory scaffolding"""

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

JOB_DESCRIPTION_FILE: str = "job_description.txt"
TEMPLATE_DIR: Path = Path("_template")


def _slugify_job_title(job_title: str) -> str:
    """Normalize a job title into a directory-safe slug"""
    return job_title.lower().replace(" ", "_").replace(",", "_").replace("__", "_")


def _ensure_company_dir(company_name: str) -> Path:
    """Create the company directory if missing, logging whether it was new"""
    company_dir: Path = Path(company_name)
    is_new: bool = not company_dir.exists()
    company_dir.mkdir(exist_ok=True)
    logger.info(
        f"creating {company_dir.name} folder"
        if is_new
        else f"the {company_dir.name} folder already exists, creating resume inside it"
    )
    return company_dir


def _create_job_description(job_dir: Path) -> None:
    """Touch the job_description.txt file inside the job directory"""
    (job_dir / JOB_DESCRIPTION_FILE).touch(exist_ok=False)


def copy_template(template_dir_path: Path, job_dir: Path, *, use_template: bool) -> None:
    """Copy the template directory into the job directory, if requested and available"""
    if template_dir_path.exists() and use_template:
        _ = shutil.copytree(template_dir_path, job_dir, dirs_exist_ok=True)
        logger.info(f"copying template directory from {template_dir_path} to {job_dir}")


def _make_job_dir(company_dir: Path, job_dir_name: str) -> Path | None:
    """Create the job subdirectory inside the company directory.

    Returns the job directory Path on success, or None if it already exists.
    """
    job_dir: Path = company_dir / job_dir_name
    try:
        job_dir.mkdir(exist_ok=False)
    except FileExistsError:
        logger.info(
            f"the resume folder for {job_dir_name} already exists in "
            f"{company_dir.name}, please choose a different name"
        )
        return None
    else:
        logger.info(f"creating {job_dir_name} folder")
        return job_dir


def create_dir_and_files(company_name: str, job_title: str, *, use_template: bool = True) -> None:
    """Create the directory structure for a new resume application.

    Args:
        company_name: The name of the company.
        job_title: The title of the job.
        use_template: Whether to copy the template directory contents.
    """
    job_dir_name: str = _slugify_job_title(job_title)
    company_dir: Path = _ensure_company_dir(company_name)

    job_dir: Path | None = _make_job_dir(company_dir, job_dir_name)
    if job_dir is None:
        return

    _create_job_description(job_dir)
    copy_template(TEMPLATE_DIR, job_dir, use_template=use_template)
