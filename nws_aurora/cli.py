import click
from nws_aurora import (
    get_images,
    get_latest_image,
    get_grid
)


@click.group()
def cmd():
    """
    A command-line interface for downloading forecast data for Aurora Borealis and Aurora Australis
    from the National Weather Service
    """
    pass


@cmd.command(help="All of the OVATION model images for the last 24 hours")
@click.option('--latest', is_flag=True)
@click.option('--pole', required=True, type=click.Choice(['north', 'south']))
def images(pole, latest):
    if latest:
        click.echo(get_latest_image(pole))
    else:
        click.echo(get_images(pole))


@cmd.command(help="Get auroral data in a gridded format for the entire Earth.")
def grid():
    click.echo(get_grid())
