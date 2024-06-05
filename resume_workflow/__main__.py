import click

from .helper import create_dir_and_files


@click.command()
@click.option("-c", "--company", required=True, help="company name", type=str, multiple=False)
@click.option("-j", "--job", help="job title", type=str)
def cli(company: str, job: str) -> None:
    create_dir_and_files(company, job)


if __name__ == "__main__":
    cli()
