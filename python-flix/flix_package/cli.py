import click


@click.command()
@click.argument('zipcode', default='', required=False)
def main(zipcode):
    """A command line tool to get the info on all the latest movies."""
    click.echo('{0}'.format(zipcode))
