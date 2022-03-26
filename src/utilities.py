#Imports
from os import environ
import requests
import logging


# Set up our logger
logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger()


def find_dup(l):
    """

    :param l: List of strings
    :return: duplicate values
    """
    try:
        dupes = []
        flat = [item for sublist in l for item in sublist]
        counter = len(l)-1
        for f in flat:
            if flat.count(f) > counter:
                if f not in dupes:
                    dupes.append(f)

        return list(dupes)
    except Exception as error:
        logger.error('Not able to find duplicate' +str(error))
        raise


def group_nodes(group):
    """

    :param group: group name
    :return: list of nodes
    """
    try:
        api_url = get_apiurl()
        nodes_group = requests.get(f'{api_url}/groups/{group}').json()
        return nodes_group
    except Exception as e:
        logging.error('something went wrong in finding nodes against group')
        raise e


def str_to_list(groups):
    """

    :param usr: comma separated user names
    :return: list of usernames
    """
    try:
        list_res = list(groups.split(","))
        return list_res
    except Exception as error:
        raise error


def get_apiurl():
    """

    Utility function which checks if connection URL is set as env
    if not return the default localhost
    :return: inventroy API URL
    """
    if environ.get('inventory_api_fqdn') is None:
        return 'http://127.0.0.1:8080'
    else:
        return environ.get('inventory_api_fqdn')
