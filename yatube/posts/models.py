from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя")
    slug = models.SlugField(verbose_name="Адрес")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор"
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Сообщество"
    )

    def __str__(self):
        return self.text
