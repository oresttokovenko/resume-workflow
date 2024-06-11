import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

JOB_DESCRIPTION_FILE: str = "job_description.txt"
TEMPLATE_DIR: Path = Path("_template")


def create_dir_and_files(
    company_name: str, job_title: str, use_template: bool = True
) -> None:
    job_title_str = (
        job_title.lower().replace(" ", "_").replace(",", "_").replace("__", "_")
    )

    root = Path(".")
    template_dir_path = root / TEMPLATE_DIR
    company_name_dir = Path(company_name)
    job_dir = company_name / Path(job_title_str)

    job_description = Path(JOB_DESCRIPTION_FILE)
    job_description_dir = job_dir / job_description

    try:
        # create company dir
        company_name_dir.mkdir(exist_ok=False)
        logger.info(f"creating {company_name_dir.name} folder")

        # create job dir
        job_dir.mkdir(exist_ok=False)
        logger.info(f"creating {job_dir.name} folder")

        # create job requirements file
        job_description_dir.touch(exist_ok=False)

        # if using template, copy files in _template
        if use_template and TEMPLATE_DIR.exists():
            template_files = [x.name for x in template_dir_path.iterdir()]
            for file in template_files:
                shutil.copy(TEMPLATE_DIR / file, job_dir / file)
                logger.info(f"copying {file} from template directory")

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

            # if using template, copy files in _template
            if use_template and TEMPLATE_DIR.exists():
                template_files = [x.name for x in template_dir_path.iterdir()]
                for file in template_files:
                    shutil.copy(TEMPLATE_DIR / file, job_dir / file)
                    logger.info(f"copying {file} from template directory")

        except FileExistsError:
            logger.info(
                f"The resume folder for {job_dir.name} already exists with this name in {company_name_dir.name}, please choose a different name"
            )
