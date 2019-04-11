# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class PublishVpnRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'PublishVpnRouteEntry','vpc')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PublishVpc(self):
		return self.get_query_params().get('PublishVpc')

	def set_PublishVpc(self,PublishVpc):
		self.add_query_param('PublishVpc',PublishVpc)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_VpnGatewayId(self):
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayId(self,VpnGatewayId):
		self.add_query_param('VpnGatewayId',VpnGatewayId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RouteDest(self):
		return self.get_query_params().get('RouteDest')

	def set_RouteDest(self,RouteDest):
		self.add_query_param('RouteDest',RouteDest)

	def get_NextHop(self):
		return self.get_query_params().get('NextHop')

	def set_NextHop(self,NextHop):
		self.add_query_param('NextHop',NextHop)

	def get_RouteType(self):
		return self.get_query_params().get('RouteType')

	def set_RouteType(self,RouteType):
		self.add_query_param('RouteType',RouteType)