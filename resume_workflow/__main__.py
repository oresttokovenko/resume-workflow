import click

from .helper import create_dir_and_files


@click.command()
@click.option("-c", "--company", required=True, help="company name", type=str, multiple=False)
@click.option("-j", "--job", required=True, help="job title", type=str)
@click.option(
    "-t/-T",
    "--template/--no-template",
    help="uses the template folder, if present",
    default=True,
)
def cli(company: str, job: str, template: bool) -> None:
    if template:
        create_dir_and_files(company, job)
    else:
        create_dir_and_files(company, job, use_template=False)


if __name__ == "__main__":
    cli()
