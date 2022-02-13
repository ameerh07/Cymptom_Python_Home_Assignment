from datetime import datetime
from typing import List
from dataclasses import dataclass


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

