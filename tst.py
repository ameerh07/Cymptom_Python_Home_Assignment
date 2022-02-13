import unittest
from logger import get_logger
from main import get_regions, get_instances

logger = get_logger("test log")

class Test(unittest.TestCase):

    def test_get_regions_correct(self):
        logger.info("testing get_regions correct")
        regions = get_regions()
        self.assertTrue(len(regions) > 0)
        logger.info("FINISHED testing get_regions correct")

    def test_get_regions_incorrect_access_key(self):
        logger.info("testing get_regions with incorrect access key")
        regions = get_regions(access_key="VRETGVRTEGV34RGVERTGV5")
        self.assertTrue(len(regions) == 0)
        logger.info("FINISHED testing get_regions with incorrect access key")

    def test_get_regions_incorrect_access_secret(self):
        logger.info("testing get_regions with incorrect access secret")
        regions = get_regions(secret_access="VCSWerv34vevVEW43gR534vVE4")
        self.assertTrue(len(regions) == 0)
        logger.info("FINISHED testing get_regions with incorrect access secret")

    def test_get_instances_correct(self):
        logger.info("testing get_instances correct")
        regions = get_regions()
        instances = get_instances(regions=regions)
        self.assertTrue(len(instances) > 0)
        logger.info("FINISHED testing get_instances correct")

    def test_get_instances_incorrect_access_key(self):
        logger.info("testing get_instances with incorrect access key")
        regions = get_regions()
        instances = get_instances(regions=regions, access_key="VRETGVRTEGV34RGVERTGV5")
        self.assertTrue(len(instances) == 0)
        logger.info("FINISHED testing get_instances with incorrect access key")

    def test_get_instances_incorrect_access_secret(self):
        logger.info("testing get_instances with incorrect access secret")
        regions = get_regions()
        instances = get_instances(regions=regions, secret_access="VCSWerv34vevVEW43gR534vVE4")
        self.assertTrue(len(instances) == 0)
        logger.info("FINISHED testing get_instances with incorrect access secret")

    def test_get_instances_none_regions(self):
        logger.info("testing get_instances with none regions")
        instances = get_instances()
        self.assertTrue(len(instances) == 0)
        logger.info("FINISHED testing get_instances with none regions")

    def test_get_instances_empty_regions(self):
        logger.info("testing get_instances with empty regions")
        instances = get_instances(regions=[])
        self.assertTrue(len(instances) == 0)
        logger.info("FINISHED testing get_instances with empty regions")


if __name__ == '__main__':
    unittest.main()