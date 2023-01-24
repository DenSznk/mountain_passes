from django.db import models
from mptt.models import MPTTModel

from mountain_pass.resources import PerevalStatuses
from users.models import User


class Area(MPTTModel):
    """ Область в которой находится перевал
    поле parent реализует древовидную иерархию хранения данных """

    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name="Родитель", related_name='child',
                               on_delete=models.PROTECT, )

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.title


class Cords(models.Model):
    """ Координаты перевала """

    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        verbose_name = 'Cords'
        verbose_name_plural = 'Cords'

    def __str__(self):
        return f'{self.longitude}, {self.latitude}, {self.height}'


class MountainPass(models.Model):
    """ Информация которую содержит перевал включает внешние ключи на
    модели User, PerevalAreas, Cords, Status """

    beauty_title = models.CharField(max_length=100, blank=True, null=True)
    other_titles = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100)
    connect = models.CharField(max_length=100, default='Нет информации')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=PerevalStatuses.new, choices=PerevalStatuses.choices)
    pereval_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cords = models.ForeignKey(Cords, on_delete=models.CASCADE)
    winter = models.CharField(max_length=30, verbose_name='Зима', blank=True)
    summer = models.CharField(max_length=30, verbose_name='Лето', blank=True)
    autumn = models.CharField(max_length=30, verbose_name='Осень', blank=True)
    spring = models.CharField(max_length=30, verbose_name='Весна', blank=True)

    @property
    def is_new(self):
        return self.status == PerevalStatuses.new

    class Meta:
        ordering = ['-added_at']
        verbose_name = 'Mountain Pass'
        verbose_name_plural = 'Mountain Passes'

    def __str__(self):
        return f'{self.title}, {self.status}'


class PerevalPhoto(models.Model):
    """ Фото перевала """

    img = models.ImageField(upload_to='media', blank=True)
    mountain_pass = models.ForeignKey(MountainPass, on_delete=models.CASCADE)

    def __str__(self):
        return self.mountain_pass


class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=55)
