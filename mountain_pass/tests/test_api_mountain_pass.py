from rest_framework import status
from rest_framework.reverse import reverse
from mountain_pass.models import MountainPass
from mountain_pass.serializers import MountainPassSerializer
from mountain_pass.tests.set_up import TestSetUp


class MountainAPITestCases(TestSetUp):

    def test_mountain_pass_api_list(self):
        response = self.client.get(
            reverse('mountain_pass:mountainpass-list')
        )
        serializer_data = MountainPassSerializer(self.mountain_pass_data_test, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
