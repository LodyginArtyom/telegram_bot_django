from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(verbose_name='id пользователя ')
    name = models.CharField(verbose_name='Имя пользователя', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Message(models.Model):
    profile = models.ForeignKey(to=Profile, verbose_name='Пользователь', on_delete=models.PROTECT)
    text = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(verbose_name='Время получения', auto_now_add=True)

    def __str__(self):
        return f'Сообщение от {self.profile.name} {self.pk}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
# Create your models here.
