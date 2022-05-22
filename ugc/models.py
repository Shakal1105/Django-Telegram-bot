from django.db import models

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Id user in social',
        unique=True,
    )
    name = models.TextField(
        verbose_name='User Name'
    )
    username = models.TextField(
        verbose_name='Username'
    )
    group = models.TextField(
        verbose_name='Group_id'
    )

    def __str__(self):
        return f'{self.name} #{self.external_id}#'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Message(models.Model):
    profile = models.ForeignKey(
        to = 'ugc.Profile',
        verbose_name = 'Profile',
        on_delete = models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Text'
    )
    created_at = models.DateTimeField(
        verbose_name='Time got',
        auto_now_add=True
    )
    group = models.TextField(
        verbose_name='Group_id'
    )

    def __str__(self):
        return f'Message {self.pk} from {self.profile}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'