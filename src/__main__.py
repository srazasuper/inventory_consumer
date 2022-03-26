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
    default=10,
    help="Limit to top-k results defaults to 10")
@click.option(
    "--groups", "--g",
    default="",
    help="comma separated values of N number of groups")
@click.option(
    "--sort", "--s",
    default="total_cpus",
    type=click.Choice(["total_cpus", "total_memory", "total_disk"]),
    help="How to sort the result CPU, MEMORY, DISK, defaults to CPU")
def cli(operation, limit, groups: list, sort):
    try:
        logger.info('trying operation... '+str(operation))
        if operation == 'group-overlap':
            groups = str_to_list(groups)
            list_nodes = []
            for nodes in groups:
                node_list = group_nodes(nodes)
                list_nodes.append(node_list)
            duplicates = find_dup(list_nodes)
            logger.info('List of overlapping nodes  '+ str(duplicates))#Needs Improvement as it should be a list
            return duplicates
        elif operation == 'group-resources':
            output = {}
            groups = get_group()
            for nodes in groups:
                node_list = group_nodes(nodes)
                for node in node_list:
                    stats = get_hostdata(node)
                    memory = stats.get('memtotal_mb')
                    cpus = stats.get('processor_vcpus')
                    disk_in_bytes = 0
                    available_disks = stats.get('devices')
                    for key, value in available_disks.items():
                        size_in_bytes = int(available_disks.get(key).get('sectors')) * int(available_disks.get(key).get('sectorsize'))
                        disk_in_bytes = disk_in_bytes + size_in_bytes
                        if nodes in output:
                            new_memory = output.get(nodes).get('total_memory') + memory
                            new_cpus = output.get(nodes).get('total_cpus') + cpus
                            new_disk = output.get(nodes).get('total_disk') + disk_in_bytes
                            output[nodes] = {
                                'total_memory': new_memory,
                                'total_cpus': new_cpus,
                                'total_disk': new_disk
                            }
                        else:
                            output[nodes] = {
                                'total_memory': memory,
                                'total_cpus': cpus,
                                'total_disk': disk_in_bytes
                            }
        sorted_x = sort_stats(output, sort, limit)
        logger.info("This is List of group-resource " + 'sorted by ' + sort + str(' ')+ str(sorted_x))
        return sorted_x
    except Exception as error:
        logger.info('operation of '+str(operation)+str(' Not successful'))
        raise error


def main():
    try:
        cli()
    except Exception as error:
        logging.error(f"{error}", exc_info=False)
