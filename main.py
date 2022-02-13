import boto3
import io
from logger import get_logger
from classes import Instance
from typing import List, Dict


ACCESS_KEY = ""
SECRET_ACCESS = ""

logger = get_logger("main log")

def get_regions(region_name: str = "us-east-2", access_key: str = ACCESS_KEY, secret_access: str = SECRET_ACCESS) -> List[str]:
    regions = []
    try:
        ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=access_key, aws_secret_access_key=secret_access)
        describe_regions_responce = ec2.describe_regions()
        regions = [region['RegionName'] for region in describe_regions_responce['Regions']]
        return regions
    except Exception as ex:
        logger.error(ex)
        return regions

def get_instances(regions: List[str] = None, access_key: str = ACCESS_KEY, secret_access: str = SECRET_ACCESS) -> Dict[str, List[Instance]]:
    res: Dict[str, List[Instance]] = dict()
    if regions is None:
        return res
    for region in regions:
        try:
            ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_access)
            instances = ec2.describe_instances()
            res[region] = []
            reservations = instances['Reservations']
            insts = reservations[0]['Instances']
            for instance in insts:
                res[region].append(instance)
                logger.debug(f"pulled instances from region {region}")
            
            while "NextToken" in instances:
                instances = ec2.describe_instances(NextToken=instances["NextToken"])
                reservations = instances['Reservations']
                insts = reservations[0]['Instances']
                for instance in insts:
                    res[region].append(instance)

        except Exception as ex:
            print("Can't get instances on region %s." % region)
            logger.error("Can't get instances on region %s." % region)
            logger.exception(ex)
            continue

    return res

if __name__ == "__main__":
    instances = get_instances(regions=get_regions())
    regions = instances.keys()
    for region in regions:
        for instance in instances[region]:
            if instance == []:
                continue
            else:
                tar = io.open('./chk.txt',"a", encoding="utf-8")
                tar.write(region+": ")
                tar.write(str(instance))
                tar.write('\n')
                tar.close()