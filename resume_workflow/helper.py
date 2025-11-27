import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

JOB_DESCRIPTION_FILE: str = "job_description.txt"
TEMPLATE_DIR: Path = Path("_template")


def copy_template(template_dir_path: Path, job_dir: Path, use_template: bool) -> None:
    """
    Copies the entire template directory to the job directory

    :param template_dir_path: Path to the template directory
    :param job_dir: Path to the job directory
    """
    if template_dir_path.exists() and use_template:
        shutil.copytree(template_dir_path, job_dir, dirs_exist_ok=True)
        logger.info(f"copying entire template directory from {template_dir_path} to {job_dir}")


def create_dir_and_files(company_name: str, job_title: str, use_template: bool = True) -> None:
    """
    Creates the structure for a new resume directory

    :param company_name: The name of the company
    :param job_title: The title of the job
    :param use_template: A boolean which indicates if the template dir should be used
    """
    job_title_str: str = job_title.lower().replace(" ", "_").replace(",", "_").replace("__", "_")

    company_name_dir: Path = Path(company_name)
    job_dir: Path = company_name / Path(job_title_str)

    job_description: Path = Path(JOB_DESCRIPTION_FILE)
    job_description_dir: Path = job_dir / job_description

    try:
        # create company dir
        company_name_dir.mkdir(exist_ok=False)
        logger.info(f"creating {company_name_dir.name} folder")

        # create job dir
        job_dir.mkdir(exist_ok=False)
        logger.info(f"creating {job_dir.name} folder")

        # create job requirements file
        job_description_dir.touch(exist_ok=False)

        # if using template
        copy_template(TEMPLATE_DIR, job_dir, use_template)

    except FileExistsError:
        logger.info(
            f"The {company_name_dir.name} folder already exists, attempting to create resume inside of it"
        )
        try:
            # create job dir
            job_dir.mkdir(exist_ok=False)
            logger.info(f"creating {job_dir.name} folder")

            # create job requirements file
            job_description_dir.touch(exist_ok=False)

            # if using template
            copy_template(TEMPLATE_DIR, job_dir, use_template)

        except FileExistsError:
            logger.info(
                f"The resume folder for {job_dir.name} already exists with this name"
                "in {company_name_dir.name} , please choose a different name"
            )
