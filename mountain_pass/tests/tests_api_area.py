from rest_framework import status
from rest_framework.reverse import reverse

from mountain_pass.models import Area
from mountain_pass.serializers import AreaSerializer
from mountain_pass.tests.set_up import TestSetUp


class AreaAPITestCases(TestSetUp):

    def test_area_api_list(self):
        response = self.client.get(
            reverse('mountain_pass:area-list')
        )
        serializer_data = AreaSerializer(self.area_data_test, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_area_detail_valid_data(self):
        response = self.client.get(
            reverse('mountain_pass:area-detail',
                    kwargs={'pk': self.area_test.pk})
        )
        area = Area.objects.get(pk=self.area_test.pk)
        serializer = AreaSerializer(area)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_area_detail_invalid_data(self):
        response = self.client.get(
            reverse('mountain_pass:area-detail',
                    kwargs={'pk': 9999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_area_post_valid_data(self):
        response = self.client.post(
            reverse('mountain_pass:area-list'),
            self.valid_area_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.valid_area_data['title'])

    def test_area_post_invalid_data(self):
        response = self.client.post(
            reverse('mountain_pass:area-list'),
            self.invalid_area_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_area_put_valid_data(self):
        response = self.client.put(
            reverse('mountain_pass:area-detail', kwargs={
                'pk': self.area_test.pk,
            }), data=self.valid_area_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.valid_area_data['title'])

    def test_area_put_invalid_data(self):
        response = self.client.put(
            reverse('mountain_pass:area-detail', kwargs={
                'pk': self.area_test.pk,
            }), data=self.invalid_area_data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_area_delete_ok(self):
        response = self.client.delete(
            reverse('mountain_pass:area-detail', kwargs={
                'pk': self.area_test_no_parent.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_area_cant_delete_with_child(self):
        response = self.client.delete(
            reverse('mountain_pass:area-detail', kwargs={
                'pk': 1})
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print(response.data)
        self.assertEqual(
            response.data,
            ['Cannot delete object with inherited objects']
        )
        self.assertEqual(Area.objects.count(), 2)

    def test_area_delete_not_found(self):
        response = self.client.delete(
            reverse('mountain_pass:area-detail', kwargs={
                'pk': 99999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
