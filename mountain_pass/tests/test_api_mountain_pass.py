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

    def test_mountain_pass_detail_valid_data(self):
        response = self.client.get(
            reverse('mountain_pass:mountainpass-detail',
                    kwargs={'pk': self.mountain_pass_test.pk})
        )
        mountain_pass = MountainPass.objects.get(pk=self.mountain_pass_test.pk)
        serializer = MountainPassSerializer(mountain_pass)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_mountain_pass_detail_invalid_data(self):
        response = self.client.get(
            reverse('mountain_pass:mountainpass-detail',
                    kwargs={'pk': 9999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mountain_pass_post_valid_data(self):
        response = self.client.post(
            reverse('mountain_pass:mountainpass-list'),
            self.valid_mountain_pass_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.valid_mountain_pass_data['title'])

    def test_mountain_pass_post_invalid_data(self):
        response = self.client.post(
            reverse('mountain_pass:mountainpass-list'),
            self.invalid_mountain_pass_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mountain_pass_put_valid_data(self):
        response = self.client.put(
            reverse('mountain_pass:mountainpass-detail', kwargs={
                'pk': self.mountain_pass_test.pk,
            }), data=self.valid_mountain_pass_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.valid_mountain_pass_data['title'])

    def test_mountain_pass_put_invalid_data(self):
        response = self.client.put(
            reverse('mountain_pass:mountainpass-detail', kwargs={
                'pk': self.mountain_pass_test.pk,
            }), data=self.invalid_mountain_pass_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mountain_pass_delete_ok(self):
        response = self.client.delete(
            reverse('mountain_pass:mountainpass-detail', kwargs={
                'pk': self.mountain_pass_test.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_mountain_pass_delete_not_found(self):
        response = self.client.delete(
            reverse('mountain_pass:mountainpass-detail', kwargs={
                'pk': 99999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
