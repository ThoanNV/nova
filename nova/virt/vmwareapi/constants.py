# Copyright (c) 2014 VMware, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Shared constants across the VMware driver
"""

from nova.compute import power_state
from nova.network import model as network_model

MIN_VC_VERSION = '5.1.0'
NEXT_MIN_VC_VERSION = '5.5.0'
# The minimum VC version for Neutron 'ovs' port type support
MIN_VC_OVS_VERSION = '5.5.0'

DISK_FORMAT_ISO = 'iso'
DISK_FORMAT_VMDK = 'vmdk'
DISK_FORMAT_ISCSI = 'iscsi'
DISK_FORMATS_ALL = [DISK_FORMAT_ISO, DISK_FORMAT_VMDK]

DISK_TYPE_THIN = 'thin'
CONTAINER_FORMAT_BARE = 'bare'
CONTAINER_FORMAT_OVA = 'ova'
CONTAINER_FORMATS_ALL = [CONTAINER_FORMAT_BARE, CONTAINER_FORMAT_OVA]

DISK_TYPE_SPARSE = 'sparse'
DISK_TYPE_PREALLOCATED = 'preallocated'
DISK_TYPE_STREAM_OPTIMIZED = 'streamOptimized'
DISK_TYPE_EAGER_ZEROED_THICK = 'eagerZeroedThick'

DATASTORE_TYPE_VMFS = 'VMFS'
DATASTORE_TYPE_NFS = 'NFS'
DATASTORE_TYPE_NFS41 = 'NFS41'
DATASTORE_TYPE_VSAN = 'vsan'

DEFAULT_VIF_MODEL = network_model.VIF_MODEL_E1000
DEFAULT_OS_TYPE = "other-64"
DEFAULT_ADAPTER_TYPE = "lsiLogic"
DEFAULT_DISK_TYPE = DISK_TYPE_STREAM_OPTIMIZED
DEFAULT_DISK_FORMAT = DISK_FORMAT_VMDK
DEFAULT_CONTAINER_FORMAT = CONTAINER_FORMAT_BARE

IMAGE_VM_PREFIX = "OSTACK_IMG"
SNAPSHOT_VM_PREFIX = "OSTACK_SNAP"

ADAPTER_TYPE_BUSLOGIC = "busLogic"
ADAPTER_TYPE_IDE = "ide"
ADAPTER_TYPE_LSILOGICSAS = "lsiLogicsas"
ADAPTER_TYPE_PARAVIRTUAL = "paraVirtual"

SCSI_ADAPTER_TYPES = [DEFAULT_ADAPTER_TYPE, ADAPTER_TYPE_LSILOGICSAS,
                      ADAPTER_TYPE_BUSLOGIC, ADAPTER_TYPE_PARAVIRTUAL]

SUPPORTED_FLAT_VARIANTS = ["thin", "preallocated", "thick", "eagerZeroedThick"]

EXTENSION_KEY = 'org.openstack.compute'
EXTENSION_TYPE_INSTANCE = 'instance'

# The max number of devices that can be connected to one adapter
# One adapter has 16 slots but one reserved for controller
SCSI_MAX_CONNECT_NUMBER = 15

# The max number of SCSI adaptors that could be created on one instance.
SCSI_MAX_CONTROLLER_NUMBER = 4

# This list was extracted from a file on an installation of ESX 6.5. The file
# can be found in /usr/lib/vmware/hostd/vimLocale/en/gos.vmsg
# The contents of this list should be updated whenever there is a new
# release of ESX.
VALID_OS_TYPES = set([
    'windows2019srvNext-64',
    'windows2019srv-64',
    'windows9srv-64',
    'windows8srv-64',
    'windows7srv-64',
    'longhorn-64',
    'longhorn',
    'winNetWeb',
    'winNetStandard-64',
    'winNetStandard',
    'winNetBusiness',
    'winNetEnterprise-64',
    'winNetEnterprise',
    'winNetDatacenter-64',
    'winNetDatacenter',
    'windows9-64',
    'windows9',
    'windows8-64',
    'windows8',
    'windows7-64',
    'windows7',
    'winvista-64',
    'winvista',
    'winXPPro-64',
    'winXPPro',
    'win2000Serv',
    'win2000Pro',
    'win2000AdvServ',
    'winNT',
    'win98',
    'win95',
    'win31',
    'dos',
    'amazonlinux2-64',
    'rhel8-64',
    'rhel7-64',
    'rhel7',
    'rhel6-64',
    'rhel6',
    'rhel5-64',
    'rhel5',
    'rhel4-64',
    'rhel4',
    'rhel3-64',
    'rhel3',
    'rhel2',
    'sles15-64',
    'sles12-64',
    'sles12',
    'sles11-64',
    'sles11',
    'sles10-64',
    'sles10',
    'sles-64',
    'sles',
    'centos8-64',
    'centos7-64',
    'centos6-64',
    'centos6',
    'centos-64',
    'centos',
    'debian11',
    'debian11-64',
    'debian10',
    'debian10-64',
    'debian9',
    'debian9-64',
    'debian8',
    'debian8-64',
    'debian7',
    'debian7-64',
    'debian6-64',
    'debian6',
    'debian5-64',
    'debian5',
    'debian4-64',
    'debian4',
    'suse-64',
    'suse',
    'asianux8-64',
    'asianux7-64',
    'asianux4-64',
    'asianux4',
    'asianux3-64',
    'asianux3',
    'fedora-64',
    'fedora',
    'oraclelinux8-64',
    'oraclelinux7-64',
    'oraclelinux6-64',
    'oraclelinux6',
    'oraclelinux-64',
    'oraclelinux',
    'ubuntu-64',
    'ubuntu',
    'coreos-64',
    'other5xlinux-64',
    'other5xlinux',
    'other4xlinux-64',
    'other4xlinux',
    'other3xlinux-64',
    'other3xlinux',
    'other26xlinux-64',
    'other26xlinux',
    'other24xlinux-64',
    'other24xlinux',
    'otherlinux',
    'darwin20-64',
    'darwin19-64',
    'darwin18-64',
    'darwin17-64',
    'darwin10-64',
    'darwin10',
    'darwin-64',
    'darwin',
    'darwin13-64',
    'darwin12-64',
    'darwin11-64',
    'darwin11',
    'darwin16-64',
    'darwin15-64',
    'darwin14-64',
    'freeBSD12-64',
    'freeBSD12',
    'freeBSD11-64',
    'freeBSD11',
    'freeBSD-64',
    'freeBSD',
    'netware6',
    'netware5',
    'solaris11-64',
    'solaris10-64',
    'solaris10',
    'vmkernel7',
    'vmkernel6',
    'vmkernel65',
    'vmkernel5',
    'vmkernel4',
    'other-64',
    'other',
])

POWER_STATES = {'poweredOff': power_state.SHUTDOWN,
                'poweredOn': power_state.RUNNING,
                'suspended': power_state.SUSPENDED}
