import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def create_dir_and_files(company_name: str, job_title: str | tuple) -> None:

    job_title_str = job_title.replace(" ", "_").replace(",", "_").replace("__", "_")

    company_name_dir = Path(company_name)
    job_dir = company_name / Path(job_title_str)

    resume_file_main = Path("main.typ")
    job_description = Path("job_description.txt")

    resume_dir = job_dir / resume_file_main
    job_description_dir = job_dir / job_description

    try:
        # create company dir
        company_name_dir.mkdir(exist_ok=False)
        logger.info(f"creating {company_name_dir.name} folder")

        # create job dir
        job_dir.mkdir(exist_ok=False)
        logger.info(f"creating {job_dir.name} folder")

        # create files
        resume_dir.touch(exist_ok=False)
        job_description_dir.touch(exist_ok=False)
        logger.info(f"creating resume files")

    except FileExistsError:
        logger.info(f"The {company_name_dir.name} folder already exists, attempting to create resume inside of it")
        try:
            # create job dir
            job_dir.mkdir(exist_ok=False)
            logger.info(f"creating {job_dir.name} folder")

            # create files
            resume_dir.touch(exist_ok=False)
            job_description_dir.touch(exist_ok=False)
            logger.info(f"creating resume files")

        except FileExistsError:
            logger.info(
                f"The resume folder for {job_dir.name} already exists with this name in {company_name_dir.name}, please choose a different name"
            )
