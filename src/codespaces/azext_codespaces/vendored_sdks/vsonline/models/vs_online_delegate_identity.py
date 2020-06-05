# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VSOnlineDelegateIdentity(Model):
    """Object that includes the identity of the user of a delegated access token.

    All required parameters must be populated in order to send to Azure.

    :param username: Required. The user's user name.
    :type username: str
    :param display_name: Required. The user's display name.
    :type display_name: str
    :param id: Required. The user's unique identifier which should never
     change.
    :type id: str
    """

    _validation = {
        'username': {'required': True},
        'display_name': {'required': True},
        'id': {'required': True},
    }

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VSOnlineDelegateIdentity, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.display_name = kwargs.get('display_name', None)
        self.id = kwargs.get('id', None)
