from rest_framework import status
from rest_framework.reverse import reverse

from mountain_pass.models import Cords
from mountain_pass.serializers import CordsSerializer
from mountain_pass.tests.set_up import TestSetUp


class CordsAPITestCases(TestSetUp):

    def test_cords_api_list(self):
        response = self.client.get(
            reverse('mountain_pass:cords-list')
        )
        serializer_data = CordsSerializer(self.cords_data_test, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_cords_detail_valid_data(self):
        response = self.client.get(
            reverse('mountain_pass:cords-detail',
                    kwargs={'pk': self.cords_test.pk})
        )
        cords = Cords.objects.get(pk=self.cords_test.pk)
        serializer = CordsSerializer(cords)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_cords_detail_invalid_data(self):
        response = self.client.get(
            reverse('mountain_pass:cords-detail',
                    kwargs={'pk': 99988})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cords_post_valid_data(self):
        response = self.client.post(
            reverse('mountain_pass:cords-list'),
            self.valid_cords_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['height'], self.valid_cords_data['height'])

    def test_cords_post_invalid_data(self):
        response = self.client.post(
            reverse('mountain_pass:cords-list'),
            self.invalid_cords_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cords_put_valid_data(self):
        response = self.client.put(
            reverse('mountain_pass:cords-detail', kwargs={
                'pk': self.cords_test.pk,
            }), data=self.valid_cords_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['height'], self.valid_cords_data['height'])

    def test_cords_put_invalid_data(self):
        response = self.client.put(
            reverse('mountain_pass:cords-detail', kwargs={
                'pk': self.cords_test.pk,
            }), data=self.invalid_cords_data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cords_delete_ok(self):
        response = self.client.delete(
            reverse('mountain_pass:cords-detail', kwargs={
                'pk': self.cords_test.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cords_delete_not_found(self):
        response = self.client.delete(
            reverse('mountain_pass:cords-detail', kwargs={
                'pk': 99999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
