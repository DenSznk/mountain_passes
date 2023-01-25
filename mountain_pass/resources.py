from django.db.models import IntegerChoices


class MountainPassStatuses(IntegerChoices):
    new = 1, 'новый'
    pending = 2, 'Модератор взял в работу'
    accepted = 3, 'Модерация прошла успешно'
    rejected = 4, 'Модерация прошла, информация не принята'
