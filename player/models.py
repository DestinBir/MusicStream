from django.contrib.auth.models import AbstractUser


class Visitor(AbstractUser):
    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    pass
