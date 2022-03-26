# Imports
import click
from src.utilities import *

# Set up our logger
logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger()



@click.command()
@click.argument("operation",
                type=click.Choice(["group-resources", "group-overlap"]))
@click.option(
    "--limit", "--l",
    type=click.INT,
    help="Limit to top-k results")
@click.option(
    "--groups", "--g",
    default="",
    help="comma separated values of N number of groups")
def cli(operation, limit, groups: list):
    """

    :param operation: What Operation we want to perform, its a choice
    :param limit: do you want to limit the output
    :param groups: comma separated list of group names
    :return: since its entry point, it depends upon operation type.
    """
    try:
        logger.info('trying operation... '+str(operation))
        if operation == 'group-overlap':
            groups = str_to_list(groups)
            list_nodes = []
            for nodes in groups:
                node_list = group_nodes(nodes)
                list_nodes.append(node_list)
            duplicates = find_dup(list_nodes)
            click.echo('List of duplicate nodes  '+ str(duplicates)) #Needs Improvement as it should be a list
        elif operation == 'group-resources':
            logger.info("group-resource-skjbxcskwks")

    except Exception as error:
        logger.info('operation of '+str(operation)+str(' Not successful'))
        raise error


def main():
    try:
        cli()
    except Exception as error:
        logging.error(f"{error}", exc_info=False)
