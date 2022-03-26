import mock
import os
import unittest
from src.utilities import *

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








if __name__ == '__main__':
    unittest.main()

