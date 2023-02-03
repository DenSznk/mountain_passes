from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from mountain_pass.models import Area, Cords, MountainPass, Photo


class TestSetUp(APITestCase):
    fixtures = ['area.json', 'cords.json',
                'mountain_pass.json', 'photo.json',
                'users.json'
                ]
    # Area test data
    area_data_test = Area.objects.all()
    area_test = Area.objects.get(pk=1)
    area_test_no_parent = Area.objects.get(pk=2)
    area_test_with_child = Area.objects.get(pk=1)

    valid_area_data = {
        'title': 'Test title',
    }
    invalid_area_data = {
        'title': 'Test title',
        'parent': 9999999
    }

    # cords test data
    cords_data_test = Cords.objects.all()
    cords_test = Cords.objects.get(pk=1)

    valid_cords_data = {
        'latitude': 11.11,
        'longitude': 11.11,
        'height': 1111,
    }
    invalid_cords_data = {
        'latitude': 11.11,
        'longitude': 11.11,
    }
    # mountain_pass test data

    mountain_pass_data_test = MountainPass.objects.all()
    mountain_pass_test = MountainPass.objects.get(pk=1)

    valid_mountain_pass_data = {
        "beauty_title": "Test B_title3",
        "other_titles": "Test O_title3",
        "title": "Test Title3",
        "connect": "No signal",
        "added_at": "2023-01-30T09:15:59.219Z",
        "updated_at": "2023-01-30T09:15:59.219Z",
        "status": 2,
        "area": 1,
        "user": 1,
        "cords": 1,
        "winter": "A1",
        "summer": '',
        "autumn": '',
        "spring": '',
    }
    invalid_mountain_pass_data = {
        "beauty_title": "Test B_title3",
        "other_titles": "Test O_title3",
        "title": "Test Title3",
        "connect": "No signal",
        "added_at": "2023-01-30T09:15:59.219Z",
        "updated_at": "2023-01-30T09:15:59.219Z",
        "status": 2,
        "area": 1,
        "winter": "A1",
        "summer": '',
        "autumn": '',
        "spring": '',
    }

    # Photo test data
    photo_data_test = Photo.objects.all()
    photo_test = Photo.objects.get(pk=1)
    photo = SimpleUploadedFile("photo.jpg", b"photo_content", content_type="image/jpeg")
    data = {
        'img': photo,
        'mountain_pass': mountain_pass_test.pk
    }
    valid_photo_data = {
        'img': 'media/91020E6F-1726-41DB-A719-47EC1102DE7C.png',
        'mountain_pass': 1,
    }
    invalid_photo_data = {
        'img': 'media/11111_3LVM9F2.jpg',
    }
