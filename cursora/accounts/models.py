import os

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Count
from django.dispatch import receiver
from slugify import slugify

# from mainapp.models import *

from django.db import models

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

MEDIA_URL = '/media/'
User._meta.get_field('email')._unique = True


def upload_to_profile(instance, filename):
    return '{directory}/{user}/{file}'.format(user=instance.user.username,
                                              file=filename,
                                              directory=Profile.directory)


#   TODO: Получение имени автора через instance, и корректное сохранение файлов.
def upload_to_video(instance, filename):
    return 'course/{user}/{title}/{file}'.format(file=filename,
                                                 user=instance.video_author.user.username,
                                                 title=instance.title.replace(' ', '_'))


def upload_to_course(instance, filename):
    return 'course/{user}/{file}'.format(user=instance.author.user.username,
                                         file=filename)


def profile_thumb_name(instance, filename):
    original_image_path = str(instance.profile_pic).rsplit('/', 1)[0]
    return os.path.join(original_image_path, filename)


class Profile(models.Model):
    """ Модель профилей """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="profile_user"
                                )

    subscription = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=upload_to_profile,
                                    default='media/profile_pic/usr.jpeg')
    directory = "profile_pic/"
    is_media = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    """ Модель категорий """
    title = models.CharField(max_length=100,
                             db_index=True,
                             unique=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    """ Модель комментариев """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               related_name='author')
    #    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='commentary', default="")
    text = models.TextField(max_length=1000, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Course(models.Model):
    """ Модель курсов """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=1200, db_index=True)
    preview = models.ImageField(blank=True, upload_to=upload_to_course, default='course/preview.png')
    date_pub = models.DateTimeField(auto_now_add=True)
    directory = "course_preview"

    def __str__(self):
        return self.title


#   TODO: #$%-> Если начнутся баги, то это из за символов
class Video(models.Model):
    """ Модель видео """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    preview = models.ImageField(blank=True, default='course/preview.png', upload_to=upload_to_video)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=1000, db_index=True, blank=True)
    video = models.FileField(blank=False, upload_to=upload_to_video)
    commentary = models.ForeignKey(Commentary, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='commentary', default="")
    date_pub = models.DateTimeField(auto_now_add=True)
    video_author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile_user.save()
