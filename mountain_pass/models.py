from django.db import models
from mptt.models import MPTTModel

from mountain_pass.resources import MountainPassStatuses
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

    def has_inherited_object(self):
        return self.child.exists()




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
    модели User, Area, Cords, Status """

    beauty_title = models.CharField(max_length=100, blank=True, null=True)
    other_titles = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100)
    connect = models.CharField(max_length=100, default='Нет информации')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=MountainPassStatuses.new, choices=MountainPassStatuses.choices)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cords = models.ForeignKey(Cords, on_delete=models.CASCADE)
    winter = models.CharField(max_length=30, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=30, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=30, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=30, verbose_name='Весна', blank=True, null=True)

    @property
    def is_new(self):
        return self.status == MountainPassStatuses.new

    class Meta:
        ordering = ['-added_at']
        verbose_name = 'Mountain Pass'
        verbose_name_plural = 'Mountain Passes'

    def __str__(self):
        return f'{self.title}, {self.status}'


class Photo(models.Model):
    """ Фото перевала """

    img = models.ImageField(upload_to='media', blank=True)
    mountain_pass = models.ForeignKey(MountainPass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mountain_pass}'


class SprActivitiesTypes(models.Model):
    """ Вид активности """
    title = models.CharField(max_length=55)
