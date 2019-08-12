#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for iosxr_lacp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: iosxr_lacp
version_added: 2.9
short_description: Manage Global Link Aggregation Control Protocol (LACP) on IOS-XR devices.
description:
  - This module manages Global Link Aggregation Control Protocol (LACP) on IOS-XR devices.
author: Nilashish Chakraborty (@nilashishc)
options:
  config:
    description: The provided configurations.
    type: dict
    suboptions:
      system:
        description: This option sets the default system parameters for LACP bundles.
        type: dict
        suboptions:
          priority:
            description:
              - The system priority to use in LACP negotiations.
              - Lower value is higher priority.
              - Refer to vendor documentation for valid values.
            type: int
          mac:
            type: dict
            description:
              - The system MAC related configuration for LACP.
            suboptions:
              address:
                description:
                  - The system ID to use in LACP negotiations.
                type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#show running-config lacp
# Tue Jul 16 17:46:08.147 UTC
# % No such configuration item(s)
#
#

- name: Merge provided configuration with device configuration
  iosxr_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
    state: merged

#
#
# -----------------------
# Module Execution Result
# -----------------------
#
# "before": {}
#
#
# "commands": [
#    "lacp system priority 10",
#    "lacp system mac 00c1.4c00.bd15"
#  ]
#
#
# "after": {
#    "system": {
#       "mac": {
#          "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#     }
#  }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:51:29.365 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#
#

# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:53:59.904 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#

- name: Replace device global lacp configuration with the given configuration
  iosxr_lacp:
    config:
      system:
        priority: 11
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#    }
#  }
#
#
# "commands": [
#    "no lacp system mac",
#    "lacp system priority 11"
#  ]
#
#
# "after": {
#    "system": {
#       "priority": 11
#    }
# }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:02:40.379 UTC
# lacp system priority 11
#
#

# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:37:09.727 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
#
#

- name: Delete global LACP configurations from the device
  iosxr_lacp:
    state: deleted

#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 11
#    }
# }
#
#
# "commands": [
#     "no lacp system mac",
#     "no lacp system priority"
# ]
#
#
# "after": {}
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:39:44.116 UTC
# % No such configuration item(s)
#
#


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lacp system priority 10', 'lacp system mac 00c1.4c00.bd15']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.iosxr.argspec.lacp.lacp import LacpArgs
from ansible.module_utils.network.iosxr.config.lacp.lacp import Lacp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=LacpArgs.argument_spec,
                           supports_check_mode=True)

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()