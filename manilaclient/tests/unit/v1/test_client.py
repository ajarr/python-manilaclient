# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import uuid

from keystoneclient import session

from manilaclient.tests.unit import utils
from manilaclient.v1 import client


class ClientTest(utils.TestCase):

    def test_adapter_properties(self):
        # sample of properties, there are many more
        retries = 3
        base_url = uuid.uuid4().hex

        s = session.Session()
        c = client.Client(session=s, service_catalog_url=base_url,
                          retries=retries, input_auth_token='token')

        self.assertEqual(base_url, c.client.base_url)
        self.assertEqual(retries, c.client.retries)