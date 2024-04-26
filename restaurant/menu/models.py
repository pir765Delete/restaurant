from django.db import models
from django.db.models import ImageField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<name>/<filename>
    return 'images/' + 'user_{0}/{1}'.format(instance.pinner_id, filename)


class Dish(models.Model):
    #
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

