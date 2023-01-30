from django.conf import settings
from django.test import TestCase

from mountain_pass.models import (Area, Cords, MountainPass, Photo)
from mountain_pass.serializers import (AreaSerializer, CordsSerializer, MountainPassSerializer, PhotoSerializer)
from users.models import User


class AreaSerializerTestCase(TestCase):

    @staticmethod
    def setUpClass(**kwargs):
        # The test runner sets DEBUG to False. Set to True to enable SQL logging.
        settings.DEBUG = True
        super(AreaSerializerTestCase, AreaSerializerTestCase).setUpClass()






# class AreaSerializerTestCase(TestCase):
#     @staticmethod
#     def setUpClass(**kwargs):
#         # The test runner sets DEBUG to False. Set to True to enable SQL logging.
#         settings.DEBUG = True
#         super(AreaSerializerTestCase, AreaSerializerTestCase).setUpClass()
#
#     def test_ok(self):
#         area1 = Area.objects.create(
#             title='Test area1',
#             parent=None,
#         )
#         area2 = Area.objects.create(
#             title='Test area2',
#             parent=area1,
#         )
#
#         data = AreaSerializer([area1, area2], many=True).data
#         expected_data = [
#             {
#                 'id': area1.id,
#                 'title': 'Test area1',
#                 'parent': None
#             },
#             {
#                 'id': area2.id,
#                 'title': 'Test area2',
#                 'parent': area1.id,
#             }
#         ]
#         self.assertEqual(expected_data, data)
#
#
# class CordsSerializerTestCase(TestCase):
#     @staticmethod
#     def setUpClass(**kwargs):
#         settings.DEBUG = True
#         super(CordsSerializerTestCase, CordsSerializerTestCase).setUpClass()
#
#     def test_ok(self):
#         cords1 = Cords.objects.create(
#             latitude=13.32,
#             longitude=12.32,
#             height=3000
#         )
#         cords2 = Cords.objects.create(
#             latitude=14.32,
#             longitude=11.32,
#             height=30001
#         )
#
#         data = CordsSerializer([cords1, cords2], many=True).data
#         expected_data = [
#             {
#                 'id': cords1.id,
#                 'latitude': 13.32,
#                 'longitude': 12.32,
#                 'height': 3000,
#             },
#             {
#                 'id': cords2.id,
#                 'latitude': 14.32,
#                 'longitude': 11.32,
#                 'height': 30001,
#             }
#         ]
#         # print(data)
#         # print(expected_data)
#
#         self.assertEqual(expected_data, data)
#
#
# class MountainPassSerializerTestCase(TestCase):
#     def setUp(self):
#         self.area3 = Area.objects.create(
#             title='Test area1',
#             parent=None,
#         )
#         self.area4 = Area.objects.create(
#             title='Test area2',
#             parent=None,
#         )
#
#         self.user6 = User.objects.create(
#             username='User1',
#             first_name='User1 first_name',
#             middle_name='User1 middle_name',
#             last_name='User1 last_name',
#             email='User1@email1.com',
#             phone='1231234124',
#         )
#         self.user7 = User.objects.create(
#             username='User2',
#             first_name='User2 first_name',
#             middle_name='User2 middle_name',
#             last_name='User2 last_name',
#             email='User2@email2.com',
#             phone='1231234124',
#         )
#
#         self.cords3 = Cords.objects.create(
#             latitude=13.32,
#             longitude=12.32,
#             height=3000
#         )
#         self.cords4 = Cords.objects.create(
#             latitude=14.32,
#             longitude=11.32,
#             height=30001
#         )
#
#     @staticmethod
#     def setUpClass(**kwargs):
#         settings.DEBUG = True
#         super(MountainPassSerializerTestCase, MountainPassSerializerTestCase).setUpClass()
#
#     def test_ok(self):
#         mountain_pass6 = MountainPass.objects.create(
#             beauty_title='Test B_title',
#             other_titles='Test O_title',
#             title='Test title',
#             connect='Test connect',
#             area=self.area3,
#             user=self.user6,
#             status=1,
#             cords=self.cords3,
#             winter='winter',
#             summer='winter',
#             autumn='winter',
#             spring='winter',
#         )
#         mountain_pass7 = MountainPass.objects.create(
#             beauty_title='Test B_title',
#             other_titles='Test O_title',
#             title='Test title',
#             connect='Test connect',
#             area=self.area4,
#             user=self.user7,
#             status=1,
#             cords=self.cords4,
#             winter='winter',
#             summer='winter',
#             autumn='winter',
#             spring='winter',
#         )
#
#         data = MountainPassSerializer([mountain_pass6, mountain_pass7], many=True).data
#         expected_data = [
#             {
#                 'id': mountain_pass6.id,
#                 'beauty_title': 'Test B_title',
#                 'other_titles': 'Test O_title',
#                 'title': 'Test title',
#                 'connect': 'Test connect',
#                 'area': self.area3.id,
#                 'user': 1,
#                 'status': 1,
#                 'cords': self.cords3.id,
#                 'winter': 'winter',
#                 'summer': 'winter',
#                 'autumn': 'winter',
#                 'spring': 'winter',
#             },
#             {
#                 'id': mountain_pass7.id,
#                 'beauty_title': 'Test B_title',
#                 'other_titles': 'Test O_title',
#                 'title': 'Test title',
#                 'connect': 'Test connect',
#                 'area': self.area4.id,
#                 'user': 2,
#                 'status': 1,
#                 'cords': self.cords4.id,
#                 'winter': 'winter',
#                 'summer': 'winter',
#                 'autumn': 'winter',
#                 'spring': 'winter',
#             }
#         ]
#
#         self.assertEqual(expected_data, data)
#
#
# # class MountainPassUpdateSerializerTestCase(TestCase):
# #     @staticmethod
# #     def setUpClass(**kwargs):
# #         settings.DEBUG = True
# #         super(MountainPassUpdateSerializerTestCase, MountainPassUpdateSerializerTestCase).setUpClass()
#
#
# class PhotoSerializerTestCase(TestCase):
#
#     def setUp(self):
#         ...
#
#     @staticmethod
#     def setUpClass(**kwargs):
#         settings.DEBUG = True
#         super(PhotoSerializerTestCase, PhotoSerializerTestCase).setUpClass()
#
#     def test_ok(self):
#         photo1 = Photo.objects.create(
#             img='media/imd1.png',
#             mountain_pass=1
#         )
#         photo2 = Photo.objects.create(
#             img='media/imd2.png',
#             mountain_pass=2
#         )
#         data = PhotoSerializer([photo1, photo2], many=True).data
#         expected_data = [
#             {
#                 'id': 1,
#                 'img': 'media/imd1.png',
#                 'mountain_pass': 1,
#             },
#             {
#                 'id': 2,
#                 'img': 'media/imd2.png',
#                 'mountain_pass': 2,
#             }
#         ]
#         self.assertEqual(expected_data, data)
