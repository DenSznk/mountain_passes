from django.conf import settings
from django.test import TestCase

from mountain_pass.models import Area, Cords, MountainPass, Photo
from mountain_pass.serializers import (AreaSerializer, CordsSerializer,
                                       MountainPassSerializer,
                                       MountainPassUpdateSerializer,
                                       PhotoSerializer)


class AreaSerializerTestCase(TestCase):
    fixtures = ['area.json']

    @staticmethod
    def setUpClass(**kwargs):
        # The test runner sets DEBUG to False. Set to True to enable SQL logging.
        settings.DEBUG = True
        super(AreaSerializerTestCase, AreaSerializerTestCase).setUpClass()

    def test_ok(self):
        areas = Area.objects.all()
        data = AreaSerializer(areas, many=True).data
        expected_data = [
            {
                'id': 1,
                'title': 'Test area1',
                'parent': None
            },
            {
                'id': 2,
                'title': 'Test aarea2',
                'parent': 1,
            }
        ]
        self.assertEqual(expected_data, data)


class CordsSerializerTestCase(TestCase):
    fixtures = ['cords.json', ]

    @staticmethod
    def setUpClass(**kwargs):
        settings.DEBUG = True
        super(CordsSerializerTestCase, CordsSerializerTestCase).setUpClass()

    def test_ok(self):
        cords = Cords.objects.all()
        data = CordsSerializer(cords, many=True).data
        expected_data = [
            {
                'id': 1,
                'latitude': 1234.12,
                'longitude': 1234.12,
                'height': 1234,
            },
            {
                'id': 2,
                'latitude': 4321.12,
                'longitude': 4321.12,
                'height': 1234,
            }
        ]
        self.assertEqual(expected_data, data)


#
#
class MountainPassSerializerTestCase(TestCase):
    fixtures = ['area.json', 'users.json', 'cords.json', 'mountain_pass.json']

    @staticmethod
    def setUpClass(**kwargs):
        settings.DEBUG = True
        super(MountainPassSerializerTestCase, MountainPassSerializerTestCase).setUpClass()

    def test_ok(self):
        mountain_passes = MountainPass.objects.get(pk=1)
        data = MountainPassSerializer(mountain_passes).data
        expected_data = {
            'id': 1,
            'beauty_title': 'Test B_title1',
            'other_titles': 'Test O_title1',
            'title': 'Test Title1',
            'connect': 'No signal',
            'area': 1,
            'user': 1,
            'status': 1,
            'cords': 1,
            'winter': 'A1',
            'summer': None,
            'autumn': None,
            'spring': None,
        }
        self.assertEqual(expected_data, data)


class PhotoSerializerTestCase(TestCase):
    fixtures = ['area.json', 'users.json', 'cords.json', 'mountain_pass.json', 'photo']

    @staticmethod
    def setUpClass(**kwargs):
        settings.DEBUG = True
        super(PhotoSerializerTestCase, PhotoSerializerTestCase).setUpClass()

    def test_ok(self):
        photo = Photo.objects.get(pk=1)
        data = PhotoSerializer(photo).data
        expected_data = {
            'id': 1,
            'img': '/media/91020E6F-1726-41DB-A719-47EC1102DE7C.png',
            'mountain_pass': 1,
        }
        self.assertEqual(expected_data, data)


class MountainPassUpdateSerializerTestCase(TestCase):
    fixtures = ['area.json', 'users.json', 'cords.json', 'mountain_pass.json']

    @staticmethod
    def setUpClass(**kwargs):
        settings.DEBUG = True
        super(MountainPassUpdateSerializerTestCase, MountainPassUpdateSerializerTestCase).setUpClass()

    def test_update_ok(self):
        mountain_pass_update = MountainPass.objects.get(pk=3)
        data = MountainPassUpdateSerializer(mountain_pass_update).data
        expected_data = {
            'id': 3,
            'beauty_title': 'Test B_title3',
            'other_titles': 'Test O_title3',
            'title': 'Test Title3',
            'connect': 'No signal',
            'area': 1,
            'user': 1,
            'status': 2,
            'cords': 1,
            'winter': 'A1',
            'summer': None,
            'autumn': None,
            'spring': None,
        }
        self.assertEqual(expected_data, data)
