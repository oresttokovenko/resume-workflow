"""CLI entry point for resume-workflow"""

import click

from .helper import create_dir_and_files


@click.command()
@click.option("-c", "--company", required=True, help="company name", type=str)
@click.option("-j", "--job", required=True, help="job title", type=str)
@click.option(
    "-t/-T",
    "--template/--no-template",
    help="copy template folder contents, if present",
    default=True,
)
def cli(company: str, job: str, template: bool) -> None:
    """Create a new resume directory structure for a job application"""
    create_dir_and_files(company, job, use_template=template)


if __name__ == "__main__":
    cli()
