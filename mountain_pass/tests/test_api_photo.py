from rest_framework import status
from rest_framework.reverse import reverse

from mountain_pass.models import Photo
from mountain_pass.serializers import PhotoSerializer
from mountain_pass.tests.set_up import TestSetUp


class PhotoAPITestCase(TestSetUp):

    def test_photo_api_list(self):
        response = self.client.get(
            reverse('mountain_pass:photo-list'),
        )
        serializer_data = PhotoSerializer(self.photo_data_test, many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_photo_detail_valid_data(self):
        response = self.client.get(
            reverse('mountain_pass:photo-detail',
                    kwargs={'pk': self.photo_test.pk})
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_photo_detail_invalid_data(self):
        response = self.client.get(
            reverse('mountain_pass:photo-detail',
                    kwargs={'pk': 9999999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
