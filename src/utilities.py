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

    :param usr: comma separated strings
    :return: list of strings
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


def get_group():
    """

    :return: List of groups
    """
    try:
        api_url = get_apiurl()
        groups = requests.get(f'{api_url}/groups').json()
        return groups
    except Exception as e:
        logging.error('something went wrong in finding list of groups')
        raise e

def get_hostdata(node):
    """
    Function to return list of hostdata
    :param node: Provide node name
    :return: node inventory
    """
    try:
        api_url = get_apiurl()
        node_data = requests.get(f'{api_url}/hostdata/{node}').json()
        return node_data
    except Exception as e:
        logging.error('something went wrong in finding list of node inventory')
        raise e


def sort_stats(dict_data, sort_key, limit):
    """

    :param
    dict_data: Dictionary data to sort.
    sort_key: The key used to sort

    :return: sorted json
    """
    try:
        sorted_x = sorted(dict_data, key=lambda x: dict_data[x][sort_key], reverse=True)
        k = limit
        i = 0
        final_data = []
        for item in sorted_x:
            if i < k:
              data = f"{item} = {dict_data[item]}"
              i = i +1
              final_data.append(data)
        return final_data
    except Exception as e:
        logging.error('something went wrong in sorting of node data')
        raise e
