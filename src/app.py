import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
@click.option('-nd', '--node', type=str, help='node selection', default='imanode')
def hello(name, node):
    click.echo(f'Hello {name} and {node}')