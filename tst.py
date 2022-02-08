import unittest
from main import get_regions, get_instances

class Test(unittest.TestCase):

    def test_get_regions_correct(self):
        regions = get_regions()
        self.assertTrue(len(regions) > 0)

    def test_get_regions_incorrect_access_key(self):
        regions = get_regions(aws_access_key_id="VRETGVRTEGV34RGVERTGV5")
        self.assertTrue(len(regions) == 0)

    def test_get_regions_incorrect_access_secret(self):
        regions = get_regions(aws_secret_access_key="VCSWerv34vevVEW43gR534vVE4")
        self.assertTrue(len(regions) == 0)

    def test_get_instances_correct(self):
        regions = get_regions()
        instances = get_instances(regions=regions)
        self.assertTrue(len(instances) > 0)

    def test_get_instances_incorrect_access_key(self):
        regions = get_regions()
        instances = get_instances(regions=regions, aws_access_key_id="VRETGVRTEGV34RGVERTGV5")
        self.assertTrue(len(instances) == 0)

    def test_get_instances_incorrect_access_secret(self):
        regions = get_regions()
        instances = get_instances(regions=regions, aws_secret_access_key="VCSWerv34vevVEW43gR534vVE4")
        self.assertTrue(len(instances) == 0)

    def test_get_instances_none_regions(self):
        instances = get_instances()
        self.assertTrue(len(instances) == 0)

    def test_get_instances_empty_regions(self):
        instances = get_instances(regions=[])
        self.assertTrue(len(instances) == 0)


if __name__ == '__main__':
    unittest.main()