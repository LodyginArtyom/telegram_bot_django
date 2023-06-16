from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(verbose_name='id пользователя ')
    name = models.CharField(verbose_name='Имя пользователя', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
# Create your models here.
