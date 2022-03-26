import mock
import os
import unittest
from src.utilities import *
#import mocker


sample_list = ['a','b','c']
sample_llist = [['a','b','c'], ['a','m','y'], ['a','z','x']]


class UtilityTests(unittest.TestCase):
    def test_duplicates(self):
        """
        test Duplicate amoong N number of elemnts in list
        :return: True/False
        """
        sample_duplicates = ['a']
        duplicate = find_dup(sample_llist)
        self.assertListEqual(duplicate, sample_duplicates)

    @mock.patch.dict(os.environ, {"inventory_api_fqdn": "http://8.8.8.8:3000"})
    def test_apiurl_env(self):
        """
        test if Os environmental variable 'inventory_api_fqdn' is set or not
        :return:
        """
        url = get_apiurl()
        assert url == 'http://8.8.8.8:3000'

    def test_api_default(self):
        """
        Test environmental variable not set than use default 127.0.0.1
        :return: http://127.0.0.1:8080
        """
        url = get_apiurl()
        assert url == 'http://127.0.0.1:8080'

    def test_str_to_list(self):
        """
        test with valid comma separated strings
        expects to be return as type list

        :return: TRUE if list
        """
        lt = str_to_list('x,y,z')
        assert type(lt) is list

#    def test_group_nodes(mocker, sample_list):
        """
        Test if we provide a list of group so it can find nodes from it.
        :return: TRUE if matches with the response.
        """
#        fake_resp = mocker.Mock()











if __name__ == '__main__':
    unittest.main()

