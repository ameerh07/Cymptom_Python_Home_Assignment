from dataclasses import dataclass
from datetime import datetime
from dacite import from_dict
from typing import List, Dict, Optional
import boto3
import io

@dataclass
class Monitoring:
    State: str

@dataclass
class Placement:
    AvailabilityZone: str
    GroupName: str
    Tenancy: str

@dataclass
class State:
    Code: int
    Name: str

@dataclass
class Ebs:
    AttachTime: datetime
    DeleteOnTermination: bool
    Status: str
    VolumeId: str

@dataclass
class BlockDeviceMapping:
    DeviceName: str
    Ebs: Ebs

@dataclass
class Association:
    IpOwnerId: str
    PublicDnsName: str
    PublicIp: str

@dataclass
class Attachment:
    AttachTime: datetime
    AttachmentId: str
    DeleteOnTermination: bool
    DeviceIndex: int
    Status: str
    NetworkCardIndex: int

@dataclass
class Group:
    GroupName: str
    GroupId: str

@dataclass
class PrivateIpAddress:
    Association: Association
    Primary: bool
    PrivateDnsName: str
    PrivateIpAddress: str

@dataclass
class NetworkInterface:
    Association: Association
    Attachment: Attachment
    Description: str
    Groups: List[Group]
    Ipv6Addresses: List[str]
    MacAddress: str
    NetworkInterfaceId: str
    OwnerId: str
    PrivateDnsName: str
    PrivateIpAddress: str
    PrivateIpAddresses: List[PrivateIpAddress]
    SourceDestCheck: bool
    Status: str
    SubnetId: str
    VpcId: str
    InterfaceType: str

@dataclass
class SecurityGroup:
    GroupName: str
    GroupId: str

@dataclass
class Tag:
    Key: str
    Value: str

@dataclass
class CpuOptions:
    CoreCount: int
    ThreadsPerCore: int

@dataclass
class CapacityReservationSpecification:
    CapacityReservationPreference: str

@dataclass
class HibernationOptions:
    Configured: bool

@dataclass()
class MetadataOptions:
    State: str
    HttpTokens: str
    HttpPutResponseHopLimit: int
    HttpEndpoint: str
    HttpProtocolIpv6: str

@dataclass
class EnclaveOptions:
    Enabled: bool

@dataclass
class PrivateDnsNameOptions:
    HostnameType: str
    EnableResourceNameDnsARecord: bool
    EnableResourceNameDnsAAAARecord: bool

@dataclass
class ProductCode:
    ProductCodeId: str
    ProductCodeType: str

@dataclass
class Instance:
    AmiLaunchIndex: int
    ImageId: str
    InstanceId: str
    InstanceType: str
    KeyName: str
    LaunchTime: datetime
    Monitoring: Monitoring
    Placement: Placement
    PrivateDnsName: str
    PrivateIpAddress: str
    ProductCodes: List[ProductCode]
    PublicDnsName: str
    PublicIpAddress: str
    State: State
    StateTransitionReason: str
    SubnetId: str
    VpcId: str
    Architecture: str
    BlockDeviceMappings: List[BlockDeviceMapping]
    ClientToken: str
    EbsOptimized: bool
    EnaSupport: bool
    Hypervisor: str
    NetworkInterfaces: List[NetworkInterface]
    RootDeviceName: str
    RootDeviceType: str
    SecurityGroups: List[SecurityGroup]
    SourceDestCheck: bool
    Tags: List[Tag]
    VirtualizationType: str
    CpuOptions: CpuOptions
    CapacityReservationSpecification: CapacityReservationSpecification
    HibernationOptions: HibernationOptions
    MetadataOptions: MetadataOptions
    EnclaveOptions: EnclaveOptions
    PlatformDetails: str
    UsageOperation: str
    UsageOperationUpdateTime: datetime
    PrivateDnsNameOptions: PrivateDnsNameOptions


ACCESS_KEY = ""
SECRET_ACCESS = ""

def get_regions(region_name: str = "us-east-2", access_key: str = ACCESS_KEY, secret_access: str = SECRET_ACCESS) -> List[str]:
    regions = []
    try:
        ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=access_key, aws_secret_access_key=secret_access)
        describe_regions_responce = ec2.describe_regions()
        regions = [region['RegionName'] for region in describe_regions_responce['Regions']]
        return regions
    except Exception as ex:
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
                instance_info = from_dict(data_class=Instance, data=instance)
                res[region].append(instance_info)

        except Exception as ex:
            print("Can't get instances on region %s." % region)
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
                tar.close()