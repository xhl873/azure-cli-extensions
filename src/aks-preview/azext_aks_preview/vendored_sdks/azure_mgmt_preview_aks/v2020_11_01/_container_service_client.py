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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import ContainerServiceClientConfiguration
from .operations import Operations
from .operations import ManagedClustersOperations
from .operations import AgentPoolsOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ResolvePrivateLinkServiceIdOperations
from . import models


class ContainerServiceClient(SDKClient):
    """The Container Service Client.

    :ivar config: Configuration for client.
    :vartype config: ContainerServiceClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerservice.v2020_11_01.operations.Operations
    :ivar managed_clusters: ManagedClusters operations
    :vartype managed_clusters: azure.mgmt.containerservice.v2020_11_01.operations.ManagedClustersOperations
    :ivar agent_pools: AgentPools operations
    :vartype agent_pools: azure.mgmt.containerservice.v2020_11_01.operations.AgentPoolsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.containerservice.v2020_11_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.containerservice.v2020_11_01.operations.PrivateLinkResourcesOperations
    :ivar resolve_private_link_service_id: ResolvePrivateLinkServiceId operations
    :vartype resolve_private_link_service_id: azure.mgmt.containerservice.v2020_11_01.operations.ResolvePrivateLinkServiceIdOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ContainerServiceClientConfiguration(credentials, subscription_id, base_url)
        super(ContainerServiceClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_clusters = ManagedClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.agent_pools = AgentPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resolve_private_link_service_id = ResolvePrivateLinkServiceIdOperations(
            self._client, self.config, self._serialize, self._deserialize)
