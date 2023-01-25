from rest_framework import serializers

from users.models import User
from .models import (Area, Cords,
                     MountainPass, Photo,
                     )


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id',
                  'title',
                  'parent',
                  ]


class CordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cords
        fields = ['id',
                  'latitude',
                  'longitude',
                  'height',
                  ]


class MountainPassSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    cords = serializers.PrimaryKeyRelatedField(queryset=Cords.objects.all(), )

    def validate(self, attrs):
        if not self.instance.is_new:
            raise serializers.ValidationError({
                'status': ['Изменения больше недоступны.']
            })
        return super().validate(attrs)

    class Meta:
        model = MountainPass
        fields = ['id',
                  'beauty_title',
                  'other_titles',
                  'title',
                  'connect',
                  'area',
                  'user',
                  'status',
                  'cords',
                  'winter',
                  'summer',
                  'autumn',
                  'spring',
                  ]
        extra_kwargs = {
            'added_at': {
                'read_only': True,
            },
            'status': {
                'read_only': True,
            },
        }


class PhotoSerializer(serializers.ModelSerializer):
    mountain_pass = serializers.PrimaryKeyRelatedField(queryset=MountainPass.objects.all())

    class Meta:
        model = Photo
        fields = ['id',
                  'img',
                  'mountain_pass',
                  ]
